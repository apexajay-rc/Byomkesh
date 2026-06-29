"""
Dataset Writer

Responsible for writing telemetry records to CSV files.
Creates one CSV per day.
"""

import csv
from pathlib import Path
from datetime import datetime

from config import RAW_DATASET_DIR


class DatasetWriter:

    def __init__(self):

        self.current_date = datetime.now().strftime("%Y-%m-%d")

        self.output_dir = RAW_DATASET_DIR / self.current_date

        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.csv_path = self.output_dir / "telemetry.csv"

    def write(self, record: dict):

        file_exists = self.csv_path.exists()

        with open(self.csv_path, "a", newline="") as csvfile:

            writer = csv.DictWriter(
                csvfile,
                fieldnames=record.keys()
            )

            if not file_exists:
                writer.writeheader()

            writer.writerow(record)
