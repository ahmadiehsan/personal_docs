import argparse
import fileinput
import os
from pathlib import Path

from scripts.utils.argument_validators import to_path_object


class Command:
    def __init__(self, arguments: argparse.Namespace) -> None:
        self.arguments = arguments

    def run(self) -> None:
        for root, _, files in os.walk(self.arguments.input_dir_path):
            for file in files:
                if file.endswith(".md"):
                    file_dir_path = Path(root)
                    file_name = file
                    self._convert_headlines_inplace(file_dir_path, file_name)

        print("Done")

    @staticmethod
    def _convert_headlines_inplace(file_dir_path: Path, file_name: str) -> None:
        """Will convert headline in-place, which means this method will not create any new file."""
        is_inside_a_code_block = False
        file_path = file_dir_path / file_name

        for line in fileinput.input(file_path, inplace=True):
            if line.startswith("```"):
                is_inside_a_code_block = not is_inside_a_code_block

            if line.startswith("#") and not is_inside_a_code_block:
                line = line.title()  # noqa: PLW2901

            print(line, end="")  # Will write the line into the file, not the console!


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_dir_path",
        help="An absolute path to a directory that contains .md files",
        type=lambda val: to_path_object(parser, val),
    )
    args = parser.parse_args()

    Command(args).run()
