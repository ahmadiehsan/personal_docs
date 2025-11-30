import argparse
import os
import re
from pathlib import Path

from PIL import Image

from scripts.utils.argument_validators import to_path_object


class Command:
    _jpeg_quality = 85
    _reduction_threshold_percent = 1
    _supported_formats = (".jpg", ".jpeg", ".png")
    _md_image_pattern = r"!\[.*?\]\(.*?/(.*)\)"
    _html_image_pattern = r'<img.*?src="(.*?)".*?>'
    _width_pattern = r"width\s*:\s*(\d+(?:\.\d+)?)(px|in|cm|mm|pt|em|rem)"

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
        image_infos = self._find_images(file_path)
        self._optimize_images(image_infos)
        self._convert_html_img_to_markdown(file_path, image_infos)

    def _find_images(self, file_path: Path) -> list[dict]:
        image_infos: list[dict] = []
        content = file_path.read_text()
        directory = file_path.with_suffix("")

        md_matches = re.findall(self._md_image_pattern, content)
        image_infos.extend({"path": directory / img, "is_html": False} for img in md_matches)

        html_matches = re.finditer(self._html_image_pattern, content)
        for match in html_matches:
            tag = match.group(0)
            src = match.group(1)
            width_px = self._convert_css_width_to_pixels(tag)
            image_infos.append({"path": directory / src, "is_html": True, "width_px": width_px, "tag": tag})

        return image_infos

    def _optimize_images(self, image_infos: list[dict]) -> None:
        for image_info in image_infos:
            if image_info["path"].suffix.lower() not in self._supported_formats:
                continue

            if image_info["is_html"] and image_info["width_px"]:
                self._resize_image(image_info["path"], image_info["width_px"])

            self._compress_image(image_info["path"])

    def _convert_html_img_to_markdown(self, file_path: Path, image_infos: list[dict]) -> None:
        content = file_path.read_text(encoding="UTF-8")

        for image_info in image_infos:
            if not image_info["is_html"]:
                continue

            original_tag = image_info["tag"]
            image_src = Path(*image_info["path"].parts[-2:])
            markdown_tag = f"![]({image_src})"
            content = content.replace(original_tag, markdown_tag, 1)

        file_path.write_text(content, encoding="UTF-8")

    def _resize_image(self, file_path: Path, target_width_px: int) -> None:
        img = Image.open(file_path)
        current_width, current_height = img.size

        if current_width <= target_width_px:
            return  # Image is already smaller than or equal to target width

        aspect_ratio = current_height / current_width
        new_height = int(target_width_px * aspect_ratio)
        resized_img = img.resize((target_width_px, new_height), Image.Resampling.LANCZOS)
        temp_file_path = file_path.with_suffix(file_path.suffix + ".temp")

        if file_path.suffix.lower() in (".jpg", ".jpeg"):
            resized_img.save(temp_file_path, format="JPEG", quality=self._jpeg_quality, optimize=True)
        elif file_path.suffix.lower() == ".png":
            resized_img.save(temp_file_path, format="PNG", optimize=True)
        else:
            err_msg = f"unsupported image format for resizing: {file_path.suffix}"
            raise ValueError(err_msg)

        temp_file_path.replace(file_path)
        print(
            f"Resized: {file_path!s:<50} | Before: {current_width}x{current_height} | "
            f"After: {target_width_px}x{new_height}"
        )

    def _compress_image(self, file_path: Path) -> None:
        original_size_kb = file_path.stat().st_size / 1024
        img = Image.open(file_path)
        temp_file_path = file_path.with_suffix(file_path.suffix + ".temp")  # Use temporary file to avoid data loss

        if file_path.suffix.lower() in (".jpg", ".jpeg"):
            img.save(temp_file_path, format="JPEG", quality=self._jpeg_quality, optimize=True)
        elif file_path.suffix.lower() == ".png":
            img.save(temp_file_path, format="PNG", optimize=True)
        else:
            err_msg = f"unsupported image format for compression: {file_path.suffix}"
            raise ValueError(err_msg)

        new_size_kb = temp_file_path.stat().st_size / 1024
        size_reduction_percent = ((original_size_kb - new_size_kb) / original_size_kb) * 100

        if size_reduction_percent > self._reduction_threshold_percent:
            temp_file_path.replace(file_path)
            print(
                f"Compressed: {file_path!s:<50} | Before: {original_size_kb:.2f} KB | "
                f"After: {new_size_kb:.2f} KB | Reduction: {size_reduction_percent:.1f}%"
            )
        else:
            temp_file_path.unlink()

    def _convert_css_width_to_pixels(self, width_str: str) -> int | None:
        match = re.search(self._width_pattern, width_str, re.IGNORECASE)
        if not match:
            return None

        value = float(match.group(1))
        unit = match.group(2).lower()

        dpi = 96
        conversions = {
            "px": lambda v: int(v),  # pylint: disable=unnecessary-lambda
            "in": lambda v: int(v * dpi),
            "cm": lambda v: int(v * dpi / 2.54),
            "mm": lambda v: int(v * dpi / 25.4),
            "pt": lambda v: int(v * dpi / 72),
        }
        return conversions[unit](value)


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
