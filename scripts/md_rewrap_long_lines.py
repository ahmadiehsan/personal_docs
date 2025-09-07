import argparse
import os
import re
from pathlib import Path

from scripts.utils.argument_validators import to_path_object


class Command:
    _split_by = ".?!"
    _split_on_length = 121
    _split_specials = ("**", "__", "~~")
    _md_blocks = ("```", "$$", "<script>", "</script>", "<style>", "</style>")
    _sentence_blocks = (('"', '"'), ("<", ">"), ("(", ")"), ("[", "]"), ("{", "}"))

    def __init__(self, arguments: argparse.Namespace) -> None:
        self.arguments = arguments

    def run(self) -> None:
        for root, _, files in os.walk(self.arguments.input_dir_path):
            for file in files:
                if file.endswith(".md"):
                    file_dir_path = Path(root)
                    file_path = file_dir_path / file
                    self._rewrap_long_lines_inplace(file_path)

        print("done")

    def _rewrap_long_lines_inplace(self, file_path: Path) -> None:
        """Simpler: combine paragraph lines, then split long lines, skipping code blocks and lists."""
        with file_path.open(encoding="utf-8") as f:
            lines = f.readlines()

        output_lines: list[str] = []
        paragraph: list[str] = []
        is_inside_block = False

        for line in lines:
            if is_inside_block:
                output_lines.append(line)
                continue

            if line.strip().startswith(self._md_blocks):
                self._flush_paragraph(paragraph, output_lines)
                output_lines.append(line)
                is_inside_block = not is_inside_block
                continue

            if self._is_text_line(line):
                paragraph.append(line)
            else:
                self._flush_paragraph(paragraph, output_lines)
                output_lines.append(line)

        self._flush_paragraph(paragraph, output_lines)

        with file_path.open("w", encoding="utf-8") as f:
            f.writelines(output_lines)

    def _flush_paragraph(self, paragraph: list[str], output_lines: list[str]) -> None:
        if not paragraph:
            return

        text = " ".join(line.strip() for line in paragraph)

        if len(text) >= self._split_on_length and any(c in text for c in self._split_by):
            text = self._split_sentences(text)

        output_lines.append(text + "\n")
        paragraph.clear()

    @staticmethod
    def _is_text_line(line: str) -> bool:  # noqa: C901, PLR0911
        """Return True if the line is a normal text line (not list, not headline, etc)."""
        s = line.rstrip("\n")

        # empty lines
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

        # nested text lines
        if re.match(r"^ {2,}", line):
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
        inside = {p[0]: 0 for p in self._sentence_blocks}
        open_to_close = {p[0]: p[1] for p in self._sentence_blocks}
        close_to_open = {p[1]: p[0] for p in self._sentence_blocks}

        text = line.strip()
        split_points = []

        # Find split points
        i = 0
        while i < len(text):
            char = text[i]

            # Track entering/exiting paired characters
            if char in close_to_open and inside[close_to_open[char]] > 0:
                inside[close_to_open[char]] -= 1
            elif char in open_to_close:
                inside[char] += 1

            # Check for split point (not inside any pair)
            is_split_char = char in self._split_by
            is_outside_any_block = not any(inside.values())
            starts_new_sentence = False
            if i + 4 < len(text) and text[i + 1] == " ":
                regular_start = text[i + 2].isupper()
                special_start = text[i + 4].isupper() and any(text[i + 2 :].startswith(s) for s in self._split_specials)
                starts_new_sentence = regular_start or special_start

            if is_split_char and is_outside_any_block and starts_new_sentence:
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
