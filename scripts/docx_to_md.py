import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

from scripts.utils.argument_validators import to_path_object
from scripts.utils.markdown import set_md_headline
from scripts.utils.timing import now_formatted


class Command:
    def __init__(self, arguments: argparse.Namespace) -> None:
        self.arguments = arguments

    def run(self) -> None:
        input_dir_path = self.arguments.input_dir_path
        output_dir_path = input_dir_path.parent / f"{input_dir_path.stem}__converted__{now_formatted()}"

        for root, _, files in os.walk(input_dir_path):
            for file in files:
                if file.endswith(".docx"):
                    current_dir_path = Path(root)
                    output_dir_root_path = output_dir_path
                    output_dir_rel_path = current_dir_path.relative_to(input_dir_path)
                    file_name_raw = ".".join(file.split(".")[:-1])
                    file_path = current_dir_path / file

                    self._convert_to_md(file_path, output_dir_root_path, output_dir_rel_path, file_name_raw)

        print(f"Done, the output dir saved at the {output_dir_path}")

    def _convert_to_md(
        self,
        docx_file_path: Path,
        destination_dir_root_path: Path,
        destination_dir_relative_path: Path,
        destination_file_name_raw: str,
    ) -> None:
        destination_dir_path = destination_dir_root_path / self._normalize_path(destination_dir_relative_path)
        destination_file_name = self._normalize_name(destination_file_name_raw)
        destination_file_path = destination_dir_path / f"{destination_file_name}.md"
        media_dir_path = destination_dir_path / destination_file_name
        destination_dir_path.mkdir(parents=True, exist_ok=True)

        try:
            subprocess.call(
                [
                    "/bin/pandoc",
                    str(docx_file_path),
                    "--to",
                    "markdown_strict",
                    "--extract-media",
                    str(media_dir_path),
                    "--output",
                    str(destination_file_path),
                    "--wrap",
                    "none",
                ]
            )
            print(f"Converted: {docx_file_path}")
        except subprocess.CalledProcessError as err:
            print(f"Error converting {docx_file_path}: {err.stderr}")
            sys.exit()

        self._remove_redundant_media_dir(media_dir_path)
        set_md_headline(destination_file_path, destination_file_name_raw)

    @staticmethod
    def _remove_redundant_media_dir(media_dir_path: Path) -> None:
        source = media_dir_path / "media"
        destination = media_dir_path

        if source.exists():
            # Move all contents from source to destination
            for item in source.iterdir():
                item.rename(destination / item.name)

            source.rmdir()

    def _normalize_path(self, path: Path) -> Path:
        normalized_parts = [self._normalize_name(part) for part in path.parts]
        return Path(*normalized_parts)

    @staticmethod
    def _normalize_name(name: str) -> str:
        if name == "/":
            return name

        starts_with_underscore = name.startswith("_")

        if "一Vs" not in name:
            name = re.sub(r"[\[\(][^)\]]*[\]\)]", "", name)

        name = name.replace("&", "And")
        name = name.lower()
        name = re.sub(r"[^a-z0-9]+", "_", name)
        name = name.strip("_")

        if starts_with_underscore:
            name = f"_{name}"

        return name


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_dir_path",
        help="An absolute path to a directory that contains .docx files",
        type=lambda val: to_path_object(parser, val),
    )
    args = parser.parse_args()

    Command(args).run()
