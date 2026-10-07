import json, csv
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data_file = root / "data" / "records.csv"
out_dir = root / "out"
out_dir.mkdir(exist_ok=True)

report = {"branch": "Shymbulak", "top_records": []}
if data_file.exists():
    with open(data_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                report["top_records"].append(row)

with open(out_dir / "report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print("Report built successfully.")
