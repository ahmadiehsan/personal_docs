#!/bin/bash

set -e

function restore_tabs {
  echo "----- Re-enable Markdown tabs"
  make script.md_toggle_tabs ./docs enable > /dev/null
}
trap restore_tabs EXIT

echo "----- Temporarily disabling Markdown tabs"
make script.md_toggle_tabs ./docs enable > /dev/null

echo "----- Run markdownlint (mdl)"
docker run --rm -v "$(pwd)":/data markdownlint/markdownlint ./docs

echo "----- Rewrapping long lines..."
make script.md_rewrap_long_lines ./docs

exit 1
