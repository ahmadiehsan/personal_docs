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
	uv run --no-dev mkdocs serve --livereload --dirty --open

manage.serve_dir:
	TARGET_DIRS="$(ARGS)"; \
	REGEX=$$(echo $$TARGET_DIRS | sed 's/ /|/g'); \
	TEMP_CONFIG_FILE=$$(PYTHONPATH=. uv run --no-sync scripts/build_mkdocs_config.py ./mkdocs.yaml '.plugins += {"exclude": {"regex": ["^(?!.*('"$$REGEX"'\/|_static|assets|index|.nav.yml)).*$$"]}}'); \
	uv run --no-dev mkdocs serve --livereload --dirty --open --config-file $$TEMP_CONFIG_FILE

manage.build:
	uv run --no-dev mkdocs build --strict

# =========================
# Scripts
# =====
script.dir_checker:
	uv run --only-dev dir_checker

script.python_checker:
	uv run --only-dev python_checker

script.docx_to_md:
	PYTHONPATH=. uv run --no-sync scripts/docx_to_md.py $(ARGS)

script.md_combiner:
	PYTHONPATH=. uv run --no-sync scripts/md_combiner.py $(ARGS)

script.md_dangling_images:
	PYTHONPATH=. uv run --no-sync scripts/md_dangling_images.py $(ARGS)

script.md_rewrap_long_lines:
	PYTHONPATH=. uv run --no-sync scripts/md_rewrap_long_lines.py $(ARGS)

script.md_toggle_tabs:
	PYTHONPATH=. uv run --no-sync scripts/md_toggle_tabs.py $(ARGS)

# =========================
# Help
# =====
help:
	echo "available targets:"
	grep -E '^[a-zA-Z0-9][a-zA-Z0-9._-]*:' Makefile | sort | awk -F: '{print "  "$$1}'
