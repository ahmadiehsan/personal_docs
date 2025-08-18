import argparse
import fileinput
import os
import re
from contextlib import closing
from pathlib import Path

from scripts.utils.argument_validators import to_path_object


class Command:
    _split_by = ".?!"
    _split_on_length = 121

    def __init__(self, arguments: argparse.Namespace) -> None:
        self.arguments = arguments

    def run(self) -> None:
        for root, _, files in os.walk(self.arguments.input_dir_path):
            for file in files:
                if file.endswith(".md"):
                    file_dir_path = Path(root)
                    file_name = file
                    self._rewrap_long_lines_inplace(file_dir_path, file_name)

        print("done")

    def _rewrap_long_lines_inplace(self, file_dir_path: Path, file_name: str) -> None:
        """Split long text lines at periods, in-place, skipping code blocks and lists."""
        is_inside_code_block = False
        file_path = file_dir_path / file_name

        with closing(fileinput.input(file_path, inplace=True)) as file_input:
            for line in file_input:
                if line.startswith("```"):
                    is_inside_code_block = not is_inside_code_block
                    print(line, end="")  # Will write the line into the file, not the console!
                    continue

                if (
                    len(line) >= self._split_on_length
                    and self._is_text_line(line, is_inside_code_block=is_inside_code_block)
                    and any(c in line for c in self._split_by)
                ):
                    split_line = self._split_sentences(line)
                    print(split_line)
                else:
                    print(line, end="")

    @staticmethod
    def _is_text_line(line: str, *, is_inside_code_block: bool) -> bool:  # noqa: C901, PLR0911
        """Return True if the line is a normal text line (not code, not list, not headline, not inside code block)."""
        if is_inside_code_block:
            return False

        s = line.rstrip("\n")
        if s.strip() == "":
            return False

        stripped = s.lstrip()

        # fenced code block markers
        if re.match(r"^(`{3,}|~{3,})", stripped):
            return False

        # ATX headings: #, ##, ... ###
        if re.match(r"^#{1,6}\b", stripped):
            return False

        # setext heading underline (=== or ---)
        if re.match(r"^(={2,}|-{3,})\s*$", s.strip()):
            return False

        # horizontal rule (***, ---, ___ possibly spaced)
        if re.match(r"^([*\-_])(?:\s*\1){2,}\s*$", s.strip()):
            return False

        # unordered list, ordered list (1. 2. ...), task list (- [ ], * [x])
        if re.match(r"^([*+\-]|\d+\.)\s+(\[.\]\s*)?", stripped):
            return False

        # blockquote
        if re.match(r"^>\s?", stripped):
            return False

        # indented code (tab or 4+ spaces)
        if line.startswith("\t") or re.match(r"^ {4,}", line):
            return False

        # link/reference definition: [id]: http...
        if re.match(r"^\[[^\]]+\]:\s*\S+", stripped):
            return False

        # simple markdown table row (starts with | and has another |)
        if stripped.startswith("|") and "|" in stripped[1:]:
            return False

        # HTML block start like <div> or <!--
        if re.match(r"^<(?:[a-zA-Z!/?]|!--)", stripped):  # noqa: SIM103
            return False

        return True

    def _split_sentences(self, line: str) -> str:
        """Split a line at periods (or ?!) followed by a space and a capital letter.

        Does NOT split inside quotes, angle brackets, parentheses, or brackets.
        """
        pairs = [('"', '"'), ("'", "'"), ("<", ">"), ("(", ")"), ("[", "]"), ("{", "}")]
        inside = {p[0]: 0 for p in pairs}
        open_to_close = {p[0]: p[1] for p in pairs}
        close_to_open = {p[1]: p[0] for p in pairs}

        text = line.strip()
        split_points = []

        # Find split points
        i = 0
        while i < len(text):
            char = text[i]

            # Track entering/exiting paired characters
            if char in open_to_close:
                inside[char] += 1
            elif char in close_to_open and inside[close_to_open[char]] > 0:
                inside[close_to_open[char]] -= 1

            # Check for split point (not inside any pair)
            if (
                char in self._split_by
                and i + 2 < len(text)
                and text[i + 1] == " "
                and text[i + 2].isupper()
                and all(v == 0 for v in inside.values())
            ):
                split_points.append(i + 1)  # split after the punctuation

            i += 1

        # Split the text at the found points
        if not split_points:
            return text

        result = []
        prev = 0
        for idx in split_points:
            result.append(text[prev:idx].strip())
            prev = idx

        result.append(text[prev:].strip())
        return "\n".join(part for part in result if part)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_dir_path",
        help="An absolute path to a directory that contains .md files",
        type=lambda val: to_path_object(parser, val),
    )
    args = parser.parse_args()

    Command(args).run()
