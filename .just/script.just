import "_share.just"
import "_working_dir.just"

dir_checker:
    uv run --only-dev dir_checker

python_checker:
    uv run --only-dev python_checker

just_indexer:
    uv run --only-dev just_indexer .just

docx_to_md *args:
    PYTHONPATH=. uv run --no-sync scripts/docx_to_md.py {{ args }}

md_combiner *args:
    PYTHONPATH=. uv run --no-sync scripts/md_combiner.py {{ args }}

md_dangling_images *args:
    PYTHONPATH=. uv run --no-sync scripts/md_dangling_images.py {{ args }}

md_rewrap_long_lines *args:
    PYTHONPATH=. uv run --no-sync scripts/md_rewrap_long_lines.py {{ args }}

md_toggle_tabs *args:
    PYTHONPATH=. uv run --no-sync scripts/md_toggle_tabs.py {{ args }}

md_image_optimizer *args:
    PYTHONPATH=. uv run --no-sync scripts/md_image_optimizer.py {{ args }}
