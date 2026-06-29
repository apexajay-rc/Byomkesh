"""
Simple test script for the Prometheus client.

Run:
    python test_prometheus.py
"""

from prometheus_client import PrometheusClient

client = PrometheusClient()

TEST_QUERIES = {
    "Prometheus Status": "up",
    "CPU Load (1m)": "node_load1",
    "CPU Usage (%)": '100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)',
    "Memory Available": "node_memory_MemAvailable_bytes",
    "Running Processes": "running_process_count",
    "Active User Sessions": "active_user_sessions",
    "Listening Ports": "listening_port_count",
    "Failed SSH Logins": "failed_ssh_login_count",
}


def main():

    print("=" * 60)
    print("Byomkesh Dataset Builder - Prometheus Connectivity Test")
    print("=" * 60)

    for name, query in TEST_QUERIES.items():

        value = client.query(query)

        print(f"{name:<30} : {value}")

    print("=" * 60)


if __name__ == "__main__":
    main()
