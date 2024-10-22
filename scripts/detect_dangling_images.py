import re
from pathlib import Path

# Regex patterns for Markdown and HTML image references
md_image_pattern = r"!\[.*?\]\(.*?\/(.*)\)"
html_image_pattern = r'<img.*?src="(.*?)".*?>'


def find_images_in_md(md_file):
    """Extract image paths mentioned in a .md file."""
    images = set()
    content = md_file.read_text()
    # Find all Markdown and HTML image references
    images.update(re.findall(md_image_pattern, content))
    images.update(re.findall(html_image_pattern, content))

    # Normalize paths (in case they have "./" or "../")
    assets_dir = md_file.with_suffix("")
    return {str(assets_dir / img) for img in images}


def check_images_in_directory(md_file):
    """Check images in the associated image directory."""
    assets_dir = md_file.with_suffix("")
    if not assets_dir.exists() or not assets_dir.is_dir():
        return set()

    # Collect all image files (JPG, PNG) from the image directory
    formats = ["*.jpg", "*.png", "*.gif"]
    return {str(img) for fmt in formats for img in assets_dir.glob(fmt)}


def compare_images(md_file):
    """Compare images in the .md file and image directory."""
    images_in_md = find_images_in_md(md_file)
    images_in_dir = check_images_in_directory(md_file)

    missing_in_dir = images_in_md - images_in_dir
    missing_in_md = images_in_dir - images_in_md

    if missing_in_dir or missing_in_md:
        print(f"\n===== File: {md_file}")
        if missing_in_dir:
            print("In .md but missing in directory:")
            for img in missing_in_dir:
                print(f"  - {img}")
        if missing_in_md:
            print("In directory but missing in .md:")
            for img in missing_in_md:
                print(f"  - {img}")


def main():
    docs_dir = Path("docs")

    # Iterate over all .md files recursively
    for md_file in docs_dir.rglob("*.md"):
        compare_images(md_file)

    print("Done")


if __name__ == "__main__":
    main()
