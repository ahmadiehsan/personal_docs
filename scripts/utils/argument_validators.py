import argparse
from pathlib import Path


def to_path_object(
    arg_parser: argparse.ArgumentParser, value: str, *, formats: list[str] | None = None, condition: str = "must_exists"
) -> Path:
    path = Path(value)
    formats = formats or []

    if formats and path.suffix not in formats:
        arg_parser.error(f"Unsupported format: '{path.suffix}'")

    match condition:
        case "must_exists":
            if not path.exists():
                arg_parser.error(f"The file '{value}' does not exist!")
        case "must_not_exists":
            if path.exists():
                arg_parser.error(f"The file '{value}' does exist!")
        case "no_check":
            pass
        case _:
            arg_parser.error(f"Invalid value for 'condition' arg: '{condition}'")

    return path
