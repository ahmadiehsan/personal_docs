import argparse
import os
from pathlib import Path

from PIL import Image

from scripts.utils.argument_validators import to_path_object


class Command:
    _image_extensions = (".jpg", ".jpeg", ".png")
    _jpeg_quality = 85
    _original_size_threshold_kb = 20
    _reduction_threshold_percent = 1

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
                if file.endswith(self._image_extensions):
                    file_dir_path = Path(root)
                    file_path = file_dir_path / file
                    self._process_file(file_path)

    def _process_file(self, file_path: Path) -> None:
        self._optimize_image(file_path)

    def _optimize_image(self, file_path: Path) -> None:
        original_size_kb = file_path.stat().st_size / 1024

        if original_size_kb <= self._original_size_threshold_kb:  # Skip files smaller than the threshold
            return

        try:
            img = Image.open(file_path)
            temp_file_path = file_path.with_suffix(file_path.suffix + ".temp")  # Use temporary file to avoid data loss

            # Optimization based on format
            if file_path.suffix.lower() in (".jpg", ".jpeg"):
                img.save(temp_file_path, format="JPEG", quality=self._jpeg_quality, optimize=True)
            elif file_path.suffix.lower() == ".png":
                img.save(temp_file_path, format="PNG", optimize=True)
            else:
                return

            new_size_kb = temp_file_path.stat().st_size / 1024
            size_reduction_percent = ((original_size_kb - new_size_kb) / original_size_kb) * 100

            # Only replace if optimization was successful
            if size_reduction_percent > self._reduction_threshold_percent:
                temp_file_path.replace(file_path)
                print(
                    f"Optimized: {file_path!s:<30} | Before: {original_size_kb:.2f} KB | "
                    f"After: {new_size_kb:.2f} KB | Reduction: {size_reduction_percent:.1f}%"
                )
            else:
                temp_file_path.unlink()

        except Exception as e:  # noqa: BLE001
            print(f"Error: {file_path} | {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize image sizes by compressing JPEG and PNG files.")
    parser.add_argument(
        "input_paths",
        nargs="+",
        help="One or more paths to files or directories that contain image files",
        type=lambda val: to_path_object(parser, val, formats=[".jpg", ".jpeg", ".png", ""]),
    )
    args = parser.parse_args()

    Command(args).run()
