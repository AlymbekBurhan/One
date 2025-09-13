import json
from datetime import datetime
from pathlib import Path


def load_scholarships(path: str = "scholarships.json"):
    data_path = Path(path)
    with data_path.open() as f:
        return json.load(f)


def format_entry(entry: dict) -> str:
    deadline = datetime.fromisoformat(entry["deadline"]).strftime("%B %d, %Y")
    return (
        f"{entry['university']}\n"
        f"  Scholarship: {entry['scholarship']}\n"
        f"  Deadline: {deadline}\n"
        f"  Info: {entry['website']}\n"
        f"  Notes: {entry['notes']}\n"
    )


def show_full_scholarships():
    scholarships = load_scholarships()
    scholarships.sort(key=lambda x: x["deadline"])
    for entry in scholarships:
        print(format_entry(entry))


if __name__ == "__main__":
    show_full_scholarships()
