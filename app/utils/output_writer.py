import json
import csv
from pathlib import Path


def save_json(data, output_path: Path):
    """
    Save candidates as JSON.
    """

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4
        )


def save_csv(data, output_path: Path):
    """
    Save candidates as CSV.
    """

    if not data:
        return

    keys = data[0].keys()

    with open(
        output_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=keys
        )

        writer.writeheader()
        writer.writerows(data)