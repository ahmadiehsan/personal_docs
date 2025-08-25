# =========================
# Init
# =====
.DEFAULT_GOAL := help
.SILENT:
ARGS := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
$(eval $(ARGS):;@:)  # Change the target-level arguments into do-nothing targets

# =========================
# Dependencies
# =====
dependencies.install:
	uv sync

dependencies.upgrade:
	uv sync --upgrade

dependencies.lock:
	uv lock

# =========================
# Git
# =====
git.init_hooks:
	uv run --only-dev pre-commit install
	uv run --only-dev pre-commit install --hook-type pre-push
	uv run --only-dev pre-commit install --hook-type commit-msg
	oco hook set

git.run_hooks_for_all:
	uv run --only-dev pre-commit run --all-files

# =========================
# Manage
# =====
manage.serve:
	uv run --no-dev mkdocs serve --open --dirty

manage.serve_dir:
	TARGET_DIR=$(firstword $(ARGS)); \
	TEMP_CONFIG_FILE=$$(PYTHONPATH=. uv run --no-sync scripts/build_mkdocs_config.py ./mkdocs.yaml '.plugins += {"exclude": {"regex": ["^(?!.*('"$$TARGET_DIR"'\/|_static|assets|index|.nav.yml)).*$$"]}}'); \
	uv run --no-dev mkdocs serve --open --dirty --config-file $$TEMP_CONFIG_FILE

manage.build:
	uv run --no-dev mkdocs build --strict

# =========================
# Scripts
# =====
script.dir_checker:
	uv run --only-dev dir_checker

script.python_checker:
	uv run --only-dev python_checker

script.detect_dangling_images:
	PYTHONPATH=. uv run --no-sync scripts/detect_dangling_images.py $(ARGS)

script.docx_to_md:
	PYTHONPATH=. uv run --no-sync scripts/docx_to_md.py $(ARGS)

script.md_combiner:
	PYTHONPATH=. uv run --no-sync scripts/md_combiner.py $(ARGS)

script.md_headlines_to_title:
	PYTHONPATH=. uv run --no-sync scripts/md_headlines_to_title.py $(ARGS)

script.md_rewrap_long_lines:
	PYTHONPATH=. uv run --no-sync scripts/md_rewrap_long_lines.py $(ARGS)

# =========================
# Help
# =====
help:
	echo "available targets:"
	grep -E '^[a-zA-Z0-9][a-zA-Z0-9._-]*:' Makefile | sort | awk -F: '{print "  "$$1}'
