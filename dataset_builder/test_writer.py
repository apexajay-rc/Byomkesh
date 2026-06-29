from collector import TelemetryCollector
from writer import DatasetWriter

collector = TelemetryCollector()
writer = DatasetWriter()

record = collector.collect()

writer.write(record)

print("Telemetry written successfully.")
