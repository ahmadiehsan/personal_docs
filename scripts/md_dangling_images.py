import argparse
import os
import re
from pathlib import Path

from scripts.utils.argument_validators import to_path_object


class Command:
    _md_image_directory_pattern = r"!\[.*?\]\((.*?)\/.*\)"
    _md_image_pattern = r"!\[.*?\]\(.*?\/(.*)\)"
    _html_image_pattern = r'<img.*?src="(.*?)".*?>'

    def __init__(self, arguments: argparse.Namespace) -> None:
        self.arguments = arguments

    def run(self) -> None:
        for input_path in self.arguments.input_paths:
            if input_path.is_dir():
                self._process_dir(input_path)
            elif input_path.is_file():
                self._process_file(input_path)

    def _process_dir(self, dir_path: Path) -> None:
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith(".md"):
                    file_dir_path = Path(root)
                    file_path = file_dir_path / file
                    self._process_file(file_path)

    def _process_file(self, file_path: Path) -> None:
        self._compare_images(file_path)

    def _compare_images(self, file_path: Path) -> None:
        directory = file_path.with_suffix("")
        directories_in_md = self._find_directories_in_md(file_path)
        images_in_md = self._find_images_in_md(file_path, directory)
        images_in_directory = self._check_images_in_directory(directory)

        duplicate_images_in_md = [img for img in images_in_md if images_in_md.count(img) > 1]
        missing_directories_in_md = [dir_ for dir_ in directories_in_md if dir_ != directory.name]
        missing_images_in_directory = set(images_in_md) - set(images_in_directory)
        missing_images_in_md = set(images_in_directory) - set(images_in_md)

        if any([duplicate_images_in_md, missing_directories_in_md, missing_images_in_directory, missing_images_in_md]):
            print(f"\n===== File: {file_path}")

            if duplicate_images_in_md:
                print("Duplicate images in .md:")
                for img in duplicate_images_in_md:
                    print(f"  - {img}")

            if missing_directories_in_md:
                print("Wrong directories in .md:")
                for dir_ in missing_directories_in_md:
                    print(f"  - {dir_}")

            if missing_images_in_directory:
                print("Missing images in .md:")
                for img in missing_images_in_directory:
                    print(f"  - {img}")

            if missing_images_in_md:
                print("Missing images in directory:")
                for img in missing_images_in_md:
                    print(f"  - {img}")

    def _find_directories_in_md(self, file_path: Path) -> list[str]:
        content = file_path.read_text()
        return re.findall(self._md_image_directory_pattern, content)

    def _find_images_in_md(self, file_path: Path, directory: Path) -> list[str]:
        images = []
        content = file_path.read_text()

        # Find all Markdown and HTML image references
        images.extend(re.findall(self._md_image_pattern, content))
        images.extend(re.findall(self._html_image_pattern, content))

        # Normalize paths (in case they have "./" or "../")
        return [str(directory / img) for img in images]

    @staticmethod
    def _check_images_in_directory(directory: Path) -> list[str]:
        if not directory.exists() or not directory.is_dir():
            return []

        formats = ["*.jpg", "*.png", "*.gif"]
        return [str(img) for fmt in formats for img in directory.glob(fmt)]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_paths",
        nargs="+",
        help="One or more paths to files or directories that contain .md files",
        type=lambda val: to_path_object(parser, val, formats=[".md", ""]),
    )
    args = parser.parse_args()

    Command(args).run()
