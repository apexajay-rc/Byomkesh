"""
Test Telemetry Collector
"""

from collector import TelemetryCollector

collector = TelemetryCollector()

record = collector.collect()

print("\nTelemetry Snapshot\n")

for key, value in record.items():
    print(f"{key:<35} : {value}")
