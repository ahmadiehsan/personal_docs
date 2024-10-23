from pathlib import Path


def set_md_headline(file_path: Path, headline: str) -> None:
    with file_path.open(encoding="UTF-8") as file:
        md_content = file.readlines()

    # Shift each heading one level down
    shifted_content = []
    for line in md_content:
        if line.startswith("######"):
            # It's already H6, no further shift
            shifted_content.append(line)
        elif line.startswith("#####"):
            shifted_content.append("######" + line[5:])
        elif line.startswith("####"):
            shifted_content.append("#####" + line[4:])
        elif line.startswith("###"):
            shifted_content.append("####" + line[3:])
        elif line.startswith("##"):
            shifted_content.append("###" + line[2:])
        elif line.startswith("#"):
            shifted_content.append("##" + line[1:])
        else:
            shifted_content.append(line)

    new_content = [f"# {headline}\n\n", *shifted_content]

    with file_path.open("w", encoding="UTF-8") as file:
        file.writelines(new_content)
