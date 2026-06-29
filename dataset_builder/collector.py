"""
Telemetry Collector

Responsible for collecting one complete telemetry snapshot
from Prometheus.

Returns one Python dictionary containing every metric.
"""

from datetime import datetime, timezone

from metrics import METRICS
from prometheus_client import PrometheusClient


class TelemetryCollector:

    def __init__(self):

        self.client = PrometheusClient()

    def collect(self):

        """
        Collect one telemetry snapshot.

        Returns
        -------
        dict
        """

        record = {}

        # -----------------------------------------------------
        # Metadata
        # -----------------------------------------------------

        record["timestamp"] = (
            datetime.now(timezone.utc)
            .isoformat()
        )

        # -----------------------------------------------------
        # Metrics
        # -----------------------------------------------------

        for metric in METRICS:

            if not metric.enabled:
                continue

            value = self.client.query(metric.query)

            record[metric.name] = value

        return record
