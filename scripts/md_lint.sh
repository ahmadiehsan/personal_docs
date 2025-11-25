#!/bin/bash

set -e

# Ensure at least one filename was passed
if [ "$#" -eq 0 ]; then
  echo "No paths passed. Exiting."
  exit 0
fi

# Re-enable Markdown tabs
function restore_tabs {
  make --no-print-directory script.md_toggle_tabs "$@" -- --mode enable
}
trap 'restore_tabs "$@"' EXIT

# Temporarily disable Markdown tabs
make --no-print-directory script.md_toggle_tabs "$@" -- --mode disable

# Rewrap long lines
make --no-print-directory script.md_rewrap_long_lines "$@"

# Detect dangling images
make --no-print-directory script.md_dangling_images "$@"

# Optimize images
make --no-print-directory script.img_optimizer "$@"

# Run markdownlint (mdl)
docker run --rm -v "$(pwd)":/data markdownlint/markdownlint "$@"
