
"""
Prometheus HTTP Client

Responsible for querying the Prometheus HTTP API.

This module NEVER knows about CSV files,
feature engineering, or machine learning.
"""

import requests

from config import (
    PROMETHEUS_URL,
    REQUEST_TIMEOUT,
)


class PrometheusClient:

    def __init__(self):
        self.base_url = f"{PROMETHEUS_URL}/api/v1/query"

    def query(self, promql: str):

        """
        Execute a single PromQL query.

        Returns
        -------
        float | int | None
        """

        try:

            response = requests.get(
                self.base_url,
                params={"query": promql},
                timeout=REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            payload = response.json()

            if payload["status"] != "success":
                return None

            results = payload["data"]["result"]

            if len(results) == 0:
                return None

            value = results[0]["value"][1]

            try:
                return float(value)

            except ValueError:
                return value

        except requests.RequestException:

            return None
