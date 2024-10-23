# =========================
# Init
# =====
ARGS := $(wordlist 2, $(words $(MAKECMDGOALS)), $(MAKECMDGOALS))
$(eval $(ARGS):;@:)  # Change the target-level arguments into do-nothing targets

# =========================
# Help (Put it first so that "make" without argument is like "make help")
# =====
help:
	@echo "Available targets:"
	@grep -E '^[a-zA-Z0-9][a-zA-Z0-9._-]*:' Makefile | sort | awk -F: '{print "  "$$1}'

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
# Requirements
# =====
requirements.compile:
	rm -f requirements/compiled/*.txt
	pip install -r requirements/prerequisite/pip-tools.txt
	pip-compile -v requirements/raw/dev.in -o requirements/compiled/dev.txt

requirements.install:
	pip install -r requirements/prerequisite/pip-tools.txt
	pip-sync requirements/compiled/dev.txt

# =========================
# Scripts
# =====
scripts.detect_dangling_images:
	PYTHONPATH=. python scripts/detect_dangling_images.py $(ARGS)

scripts.docx_to_md:
	PYTHONPATH=. python scripts/docx_to_md.py $(ARGS)

scripts.md_combiner:
	PYTHONPATH=. python scripts/md_combiner.py $(ARGS)

scripts.md_headlines_to_title:
	PYTHONPATH=. python scripts/md_headlines_to_title.py $(ARGS)

# =========================
# App (Main Application)
# =====
app.serve:
	mkdocs serve --open --dirty

app.build:
	mkdocs build --strict
