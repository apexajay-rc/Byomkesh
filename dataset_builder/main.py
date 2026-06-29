"""
Dataset Builder Main Loop
"""

import time

from collector import TelemetryCollector
from writer import DatasetWriter
from metadata import MetadataManager
from logger import logger

from config import SCRAPE_INTERVAL


collector = TelemetryCollector()

writer = DatasetWriter()

metadata = MetadataManager()

metadata.create()

logger.info("Dataset Builder started.")


while True:

    try:

        record = collector.collect()

        writer.write(record)

        logger.info("Collected telemetry snapshot.")

    except Exception as e:

        logger.exception(e)

    time.sleep(SCRAPE_INTERVAL)
