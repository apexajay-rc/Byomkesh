"""
Dataset Metadata Generator
"""

from pathlib import Path
from datetime import datetime
import platform
import socket
import yaml

from config import (
    RAW_DATASET_DIR,
    SCRAPE_INTERVAL,
    COLLECTOR_VERSION,
    SCHEMA_VERSION,
)


class MetadataManager:

    def __init__(self):

        today = datetime.now().strftime("%Y-%m-%d")

        self.output_dir = RAW_DATASET_DIR / today

        self.output_dir.mkdir(parents=True, exist_ok=True)

        self.metadata_file = self.output_dir / "metadata.yaml"

    def create(self):

        if self.metadata_file.exists():
            return

        metadata = {

            "schema_version": SCHEMA_VERSION,

            "collector_version": COLLECTOR_VERSION,

            "sampling_interval_seconds": SCRAPE_INTERVAL,

            "hostname": socket.gethostname(),

            "os": platform.platform(),

            "kernel": platform.release(),

            "created": datetime.utcnow().isoformat(),

            "label": "normal",

            "dataset_type": "baseline"

        }

        with open(self.metadata_file, "w") as file:

            yaml.dump(metadata, file, sort_keys=False)
