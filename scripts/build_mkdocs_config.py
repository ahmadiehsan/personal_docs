import argparse
import copy
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class ModificationCommand:
    """Represents a parsed modification command."""

    path_keys: list[str]
    value: Any


class Command:
    def __init__(self, arguments: argparse.Namespace) -> None:
        self.arguments = arguments

    def run(self) -> None:
        command = self._parse_command()
        initial_data = self._read_yaml()
        modified_data = self._apply_changes(initial_data, command)
        output_path = self._write_yaml(modified_data)
        print(output_path)  # Print final path to stdout for scripting

    def _parse_command(self) -> ModificationCommand:
        path_str, value_yaml = [s.strip() for s in self.arguments.command.split("+=", 1)]
        if not path_str.startswith("."):
            err_msg = "invalid command syntax: Path must start with a dot (e.g., '.plugins')"
            raise ValueError(err_msg)

        try:
            value_to_add = yaml.safe_load(value_yaml)
        except yaml.YAMLError as e:
            err_msg = f"invalid command syntax: {e}"
            raise ValueError(err_msg) from e

        keys = path_str.strip(".").split(".")
        return ModificationCommand(path_keys=keys, value=value_to_add)

    def _read_yaml(self) -> dict[str, Any]:
        with self.arguments.mkdocs_file.open("r") as f:
            return yaml.safe_load(f)

    def _write_yaml(self, data: dict[str, Any]) -> Path:
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".yml", dir="/tmp") as tmp_file:
            yaml.dump(data, tmp_file, sort_keys=False, indent=2)
            return Path(tmp_file.name)

    def _apply_changes(self, data: dict[str, Any], command: ModificationCommand) -> dict[str, Any]:
        modified_data = copy.deepcopy(data)
        target = modified_data

        # Apply the user's command (e.g., adding a plugin)
        for key in command.path_keys[:-1]:
            target = target.setdefault(key, {})

        target_list_key = command.path_keys[-1]
        target_list = target.setdefault(target_list_key, [])

        if not isinstance(target_list, list):
            err_msg = f"path '.{''.join(command.path_keys)}' is not a list"
            raise TypeError(err_msg)

        if isinstance(command.value, list):
            target_list.extend(command.value)
        else:
            target_list.append(command.value)

        # Add custom docs_dir
        project_root = self.arguments.mkdocs_file.resolve().parent
        relative_docs_dir = modified_data.get("docs_dir", "docs")
        absolute_docs_dir = project_root / relative_docs_dir
        modified_data["docs_dir"] = str(absolute_docs_dir)

        return modified_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mkdocs_file", type=Path, help="The path to the mkdocs YAML file (e.g., mkdocs.yaml).")
    parser.add_argument("command", type=str, help="The command string in '.path += value' format.")
    args = parser.parse_args()

    Command(args).run()
