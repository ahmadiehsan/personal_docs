import ast

from scripts.file_checker._dto import FileSpecsDto

_TStrVars = dict[str, tuple[str, int]]


class MsgValidator:
    def validate(self, tree: ast.AST, file_specs: FileSpecsDto) -> None:
        variables = self._collect_str_vars(tree)

        for node in ast.walk(tree):
            # Check for logging calls
            log_funcs = {"info", "debug", "error", "warning", "critical"}
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in log_funcs:
                self._check_node(node.args, variables, "log", file_specs)

            # Check for exception raises
            if isinstance(node, ast.Raise) and isinstance(node.exc, ast.Call):
                self._check_node(node.exc.args, variables, "exception", file_specs)

    def _collect_str_vars(self, tree: ast.AST) -> _TStrVars:
        """Collect variables mapped to their first assigned string constant."""
        variables: _TStrVars = {}

        for node in ast.walk(tree):
            if not isinstance(node, ast.Assign):
                continue

            for target in node.targets:
                if not isinstance(target, ast.Name):
                    continue

                key = self._unique_key(target)
                strings = self._get_strings(node.value)

                if strings:
                    variables[key] = strings[0]

        return variables

    def _unique_key(self, node: ast.Name) -> str:
        scope = self._get_scope(node)
        return f"{scope}__{node.id}"

    @staticmethod
    def _get_scope(node: ast.Name) -> str:
        is_cls_or_func = ast.FunctionDef | ast.ClassDef | ast.AsyncFunctionDef
        current: ast.AST | None = node

        for _ in range(10):  # Check up to limited levels
            if current is None:
                break

            if isinstance(current, is_cls_or_func):
                return current.name

            current = current.parent  # type: ignore[attr-defined]

        return "global"

    @staticmethod
    def _get_strings(node: ast.AST) -> list[tuple[str, int]]:
        """Extract string constants and their line numbers from an AST node."""
        strings: list[tuple[str, int]] = []

        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            strings.append((node.value, node.lineno))
        if isinstance(node, ast.JoinedStr):
            strings.extend(
                (part.value, part.lineno)
                for part in node.values
                if isinstance(part, ast.Constant) and isinstance(part.value, str)
            )

        return strings

    def _check_node(self, args: list[ast.expr], variables: _TStrVars, category: str, file_specs: FileSpecsDto) -> None:
        """Check if string arguments start with uppercase."""
        for arg in args:
            if not isinstance(arg, ast.Name):
                strings = self._get_strings(arg)
            else:
                key = self._unique_key(arg)
                strings = [variables[key]] if key in variables else []

            for string, line in strings:
                if string and string[0].isupper():
                    error = f"{file_specs.rel_path}:{line}: {category} '{string}' starts with uppercase"
                    file_specs.errors.append(error)

                if string and string[-1] in (".", ":", "?", "!"):
                    error = f"{file_specs.rel_path}:{line}: {category} '{string}' ends with punctuation"
                    file_specs.errors.append(error)
