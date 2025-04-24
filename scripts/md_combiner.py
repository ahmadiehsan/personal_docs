import argparse
import re
import shutil
from pathlib import Path
from uuid import uuid4

from scripts.utils.argument_validators import to_path_object
from scripts.utils.markdown import set_md_headline


class Command:
    def __init__(self, arguments: argparse.Namespace) -> None:
        self.arguments = arguments

    def run(self) -> None:
        input_file_paths = self.arguments.input_file_path
        output_file_path = self.arguments.output_file_path

        output_assets_temp_dir_path = output_file_path.parent / str(uuid4())
        output_assets_dir_path = output_file_path.parent / output_file_path.stem

        with output_file_path.open("w", encoding="UTF-8") as output_file:
            for input_file_path in input_file_paths:
                with input_file_path.open(encoding="UTF-8") as input_file:
                    content = input_file.read()

                    input_assets_dir_path = input_file_path.parent / input_file_path.stem
                    if input_assets_dir_path.exists():
                        content = self._move_assets(
                            content, input_assets_dir_path, output_assets_dir_path, output_assets_temp_dir_path
                        )

                    output_file.write(content)
                    output_file.write("\n")

        headline = output_file_path.stem.replace("_", " ").title()
        set_md_headline(output_file_path, headline)

        if output_assets_dir_path.exists():
            output_assets_dir_path.rename(output_assets_dir_path.parent / f"{output_assets_dir_path.name}__old")

        output_assets_temp_dir_path.rename(output_assets_dir_path)

        print("done")

    @staticmethod
    def _move_assets(md_content: str, input_dir_path: Path, output_dir_path: Path, output_dir_path_temp: Path) -> str:
        output_dir_path_temp.mkdir(parents=True, exist_ok=True)

        for input_item_path in input_dir_path.iterdir():
            input_item_name = input_item_path.name
            output_item_name = input_item_name
            output_item_path = output_dir_path_temp / output_item_name

            # Rename if the file already exists
            count = 1
            while output_item_path.exists():
                if re.match(r"image\d*\..{2,4}", output_item_name):
                    extension = output_item_name.split(".")[-1]
                    output_item_name = f"image{count}.{extension}"
                else:
                    output_item_name = f"{input_item_path.stem}_{count}{input_item_path.suffix}"

                output_item_path = output_dir_path_temp / output_item_name
                count += 1

            # Copy the file
            shutil.copy(input_item_path, output_item_path)

            # Replace for short names
            input_item_short_path = Path(input_dir_path.name) / input_item_name
            output_item_short_path = Path(output_dir_path.name) / output_item_name
            md_content = md_content.replace(str(input_item_short_path), str(output_item_short_path))

            # Replace for only names
            md_content = md_content.replace(input_item_name, output_item_name)

        return md_content


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file_path",
        help="An absolute path to a .md file",
        nargs="+",
        type=lambda val: to_path_object(parser, val, formats=[".md"]),
    )
    parser.add_argument(
        "output_file_path",
        help="An absolute path to a .md file",
        type=lambda val: to_path_object(parser, val, formats=[".md"], condition="must_not_exists"),
    )
    args = parser.parse_args()

    Command(args).run()
