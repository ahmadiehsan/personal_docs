#!/bin/bash

set -e

# Ensure at least one filename was passed
if [ "$#" -eq 0 ]; then
  echo "No paths passed. Exiting."
  exit 0
fi

# Re-enable Markdown tabs
function restore_tabs {
  just script md_toggle_tabs "$@" --mode enable
}
trap 'restore_tabs "$@"' EXIT

# Temporarily disable Markdown tabs
just script md_toggle_tabs "$@" --mode disable

# Rewrap long lines
just script md_rewrap_long_lines "$@"

# Detect dangling images
just script md_dangling_images "$@"

# Optimize images
just script md_image_optimizer "$@"

# Run markdownlint (mdl)
docker run --rm -v "$(pwd)":/data markdownlint/markdownlint "$@"
