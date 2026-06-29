"""
Configuration for the Byomkesh Dataset Builder.
"""

from pathlib import Path

# ---------------------------------------------------------------------
# Prometheus Configuration
# ---------------------------------------------------------------------

PROMETHEUS_URL = "http://localhost:9090"

# How often to collect data (seconds)
SCRAPE_INTERVAL = 10

# HTTP timeout (seconds)
REQUEST_TIMEOUT = 5

# ---------------------------------------------------------------------
# Dataset Configuration
# ---------------------------------------------------------------------

DATASET_ROOT = Path("datasets")

RAW_DATASET_DIR = DATASET_ROOT / "raw"

PROCESSED_DATASET_DIR = DATASET_ROOT / "processed"

FEATURE_DATASET_DIR = DATASET_ROOT / "features"

LABEL_DATASET_DIR = DATASET_ROOT / "labels"

METADATA_FILENAME = "metadata.yaml"

SCHEMA_VERSION = "1.0.0"

COLLECTOR_VERSION = "1.0.0"

# ---------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------

LOG_DIR = Path("logs")

LOG_FILE = LOG_DIR / "collector.log"

LOG_LEVEL = "INFO"

# ---------------------------------------------------------------------
# Host Information
# ---------------------------------------------------------------------

HOSTNAME = None  # Auto-detect

OS_NAME = None   # Auto-detect

KERNEL_VERSION = None  # Auto-detect
