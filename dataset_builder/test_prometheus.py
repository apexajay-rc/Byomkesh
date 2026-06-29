from prometheus_client import PrometheusClient

client = PrometheusClient()

print(client.query("up"))
