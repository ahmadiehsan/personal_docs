# =========================
# Init
# =====
.DEFAULT_GOAL := help
ARGS := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
$(eval $(ARGS):;@:)  # Change the target-level arguments into do-nothing targets

# =========================
# Requirements
# =====
requirements.compile:
	pip install -q poetry==2.1.2
	poetry update

requirements.install:
	pip install -q poetry==2.1.2
	poetry install

# =========================
# PreCommit
# =====
pre_commit.init:
	pre-commit install
	pre-commit install --hook-type pre-push
	pre-commit install --hook-type commit-msg
	oco hook set

pre_commit.run_for_all:
	pre-commit run --all-files

# =========================
# Manage
# =====
manage.serve:
	mkdocs serve --open --dirty

manage.build:
	mkdocs build --strict

# =========================
# Scripts
# =====
script.file_checker: _is_env_dev
	PYTHONPATH=. python scripts/file_checker/file_checker.py

script.dir_checker: _is_env_dev
	PYTHONPATH=. python scripts/dir_checker/dir_checker.py

script.detect_dangling_images:
	PYTHONPATH=. python scripts/detect_dangling_images.py $(ARGS)

script.docx_to_md:
	PYTHONPATH=. python scripts/docx_to_md.py $(ARGS)

script.md_combiner:
	PYTHONPATH=. python scripts/md_combiner.py $(ARGS)

script.md_headlines_to_title:
	PYTHONPATH=. python scripts/md_headlines_to_title.py $(ARGS)

# =========================
# Help
# =====
help:
	@echo "Available targets:"
	@grep -E '^[a-zA-Z0-9][a-zA-Z0-9._-]*:' Makefile | sort | awk -F: '{print "  "$$1}'
