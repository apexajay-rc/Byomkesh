"""
Logging configuration
"""

import logging

from config import LOG_DIR, LOG_FILE, LOG_LEVEL

LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(

    filename=LOG_FILE,

    level=LOG_LEVEL,

    format="%(asctime)s | %(levelname)s | %(message)s"

)

logger = logging.getLogger("dataset_builder")
