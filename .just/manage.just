import "_share.just"
import "_working_dir.just"

serve:
    uv run --no-dev mkdocs serve --livereload --dirty --open

serve_dirs +dirs:
    #!/usr/bin/env sh
    regex=$(printf '%s' "{{ dirs }}" | sed 's/ /|/g')
    temp_config_file="$(
        PYTHONPATH=. uv run --no-sync scripts/build_mkdocs_config.py ./mkdocs.yaml \
          '.plugins += {"exclude": {"regex": ["^(?!.*('"$regex"'\/|_static|assets|index|.nav.yml)).*$"]}}'
    )"
    trap 'rm -f "$temp_config_file"' EXIT INT TERM
    uv run --no-dev mkdocs serve --livereload --dirty --open --config-file "$temp_config_file"

build:
    uv run --no-dev mkdocs build --strict
