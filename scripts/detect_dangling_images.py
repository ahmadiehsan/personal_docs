import re
from pathlib import Path


class Command:
    md_image_directory_pattern = r"!\[.*?\]\((.*?)\/.*\)"
    md_image_pattern = r"!\[.*?\]\(.*?\/(.*)\)"
    html_image_pattern = r'<img.*?src="(.*?)".*?>'

    def run(self) -> None:
        docs_directory = Path("docs")

        # Iterate over all .md files recursively
        for md_file in docs_directory.rglob("*.md"):
            self._compare_images(md_file)

        print("done")

    def _compare_images(self, md_file: Path) -> None:
        directory = md_file.with_suffix("")
        directories_in_md = self._find_directories_in_md(md_file)
        images_in_md = self._find_images_in_md(md_file, directory)
        images_in_directory = self._check_images_in_directory(directory)

        duplicate_images_in_md = [img for img in images_in_md if images_in_md.count(img) > 1]
        missing_directories_in_md = [dir_ for dir_ in directories_in_md if dir_ != directory.name]
        missing_images_in_directory = set(images_in_md) - set(images_in_directory)
        missing_images_in_md = set(images_in_directory) - set(images_in_md)

        if any([duplicate_images_in_md, missing_directories_in_md, missing_images_in_directory, missing_images_in_md]):
            print(f"\n===== File: {md_file}")

            if duplicate_images_in_md:
                print("duplicate images in .md:")
                for img in duplicate_images_in_md:
                    print(f"  - {img}")

            if missing_directories_in_md:
                print("wrong directories in .md:")
                for dir_ in missing_directories_in_md:
                    print(f"  - {dir_}")

            if missing_images_in_directory:
                print("missing images in .md:")
                for img in missing_images_in_directory:
                    print(f"  - {img}")

            if missing_images_in_md:
                print("missing images in directory:")
                for img in missing_images_in_md:
                    print(f"  - {img}")

    def _find_directories_in_md(self, md_file: Path) -> list[str]:
        content = md_file.read_text()

        return re.findall(self.md_image_directory_pattern, content)

    def _find_images_in_md(self, md_file: Path, directory: Path) -> list[str]:
        images = []
        content = md_file.read_text()

        # Find all Markdown and HTML image references
        images.extend(re.findall(self.md_image_pattern, content))
        images.extend(re.findall(self.html_image_pattern, content))

        # Normalize paths (in case they have "./" or "../")
        return [str(directory / img) for img in images]

    @staticmethod
    def _check_images_in_directory(directory: Path) -> list[str]:
        if not directory.exists() or not directory.is_dir():
            return []

        formats = ["*.jpg", "*.png", "*.gif"]
        return [str(img) for fmt in formats for img in directory.glob(fmt)]


if __name__ == "__main__":
    Command().run()
