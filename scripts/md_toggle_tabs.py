import argparse
import os
from pathlib import Path

from scripts.utils.argument_validators import to_path_object


class Command:
    _tab_indent = "    "
    _tab_indent_count = len(_tab_indent)
    _tab_start_marker = "=== "
    _tab_end_marker = "[[[end_of_tab]]]"

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
        self._toggle_tabs_inplace(file_path)

    def _toggle_tabs_inplace(self, file_path: Path) -> None:
        with file_path.open(encoding="utf-8") as f:
            content = f.read()

        if not self._should_process(content):
            return

        lines = content.splitlines(keepends=True)
        output_lines = self._process_lines(lines)

        with file_path.open("w", encoding="utf-8") as f:
            f.writelines(output_lines)

    def _should_process(self, content: str) -> bool:
        tab_condition = self._tab_start_marker in content
        disable_condition = self.arguments.mode == "disable" and self._tab_end_marker not in content
        enable_condition = self.arguments.mode == "enable" and self._tab_end_marker in content
        return tab_condition and (disable_condition or enable_condition)

    def _process_lines(self, lines: list[str]) -> list[str]:
        output_lines: list[str] = []
        is_in_tab = False

        for i, line in enumerate(lines):
            stripped_line = line.strip()

            if stripped_line.startswith(self._tab_start_marker):
                is_in_tab = True
                output_lines.append(line)
                continue

            if is_in_tab:
                if self.arguments.mode == "disable":
                    is_in_tab = self._process_disable_mode(line, i, lines, output_lines)
                elif self.arguments.mode == "enable":
                    is_in_tab = self._process_enable_mode(line, output_lines)
            else:
                output_lines.append(line)

        return output_lines

    def _process_disable_mode(self, line: str, line_index: int, lines: list[str], output_lines: list[str]) -> bool:
        if line.startswith(self._tab_indent):
            output_lines.append(line[self._tab_indent_count :])
        else:
            output_lines.append(line)

        try:
            next_line = lines[line_index + 1]
        except IndexError:
            next_line = None

        if next_line is None:
            output_lines.append("\n")
            output_lines.append(f"{self._tab_end_marker}\n")
            return False

        if next_line.strip() and not next_line.startswith(self._tab_indent):
            output_lines.append(f"{self._tab_end_marker}\n")
            output_lines.append("\n")
            return False

        return True

    def _process_enable_mode(self, line: str, output_lines: list[str]) -> bool:
        stripped_line = line.strip()

        if stripped_line == self._tab_end_marker:
            self._remove_extra_empty_line(output_lines)
            return False

        if not stripped_line:
            output_lines.append("\n")
        else:
            output_lines.append(f"{self._tab_indent}{line}")
        return True

    def _remove_extra_empty_line(self, output_lines: list[str]) -> None:
        if not output_lines:
            err_msg = "output_lines is empty"
            raise ValueError(err_msg)

        last_element = output_lines[-1]

        if last_element == "\n":
            output_lines.pop()  # Remove the last empty line
        else:
            err_msg = f"expected last element to be '\\n', got {last_element}"
            raise ValueError(err_msg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_paths",
        nargs="+",
        help="One or more paths to files or directories that contain .md files",
        type=lambda val: to_path_object(parser, val, formats=[".md", ""]),
    )
    parser.add_argument(
        "--mode",
        choices=["enable", "disable"],
        required=True,
        help="Mode to process tabs: 'enable' to add indentation, 'disable' to remove indentation",
    )
    args = parser.parse_args()

    Command(args).run()
