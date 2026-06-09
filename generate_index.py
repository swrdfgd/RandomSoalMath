import json
import re
from pathlib import Path

ROOT = Path("questions")

catalog = {}

for category_dir in ROOT.iterdir():
    if not category_dir.is_dir():
        continue

    question_files = []

    for file in category_dir.iterdir():
        if not file.is_file():
            continue

        if re.fullmatch(r"q\d+\.json", file.name):
            question_files.append(file.name)

    question_files.sort(
        key=lambda x: int(re.search(r"\d+", x).group())
    )

    index_data = {
        "count": len(question_files),
        "files": question_files
    }

    with open(
        category_dir / "index.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            index_data,
            f,
            ensure_ascii=False,
            indent=2
        )

    catalog[category_dir.name] = len(question_files)

with open(
    ROOT / "catalog.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        catalog,
        f,
        ensure_ascii=False,
        indent=2
    )

print("Selesai.")
print(f"Kategori: {len(catalog)}")
print(f"Total soal: {sum(catalog.values())}")