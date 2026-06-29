"""
Metric Registry

This module defines every metric collected by the Dataset Builder.

Each metric contains:

- name
- PromQL query
- category
- datatype
- unit
- description
- required
- enabled
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Metric:

    name: str
    query: str
    category: str
    datatype: str
    unit: str
    description: str
    required: bool = True
    enabled: bool = True


METRICS = [

    # ==============================================================
    # CPU
    # ==============================================================

    Metric(
        name="cpu_usage_percent",
        query='100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)',
        category="cpu",
        datatype="float",
        unit="percent",
        description="Overall CPU utilization percentage"
    ),

    Metric(
        name="load_average_1m",
        query="node_load1",
        category="cpu",
        datatype="float",
        unit="load",
        description="1 minute load average"
    ),

    Metric(
        name="load_average_5m",
        query="node_load5",
        category="cpu",
        datatype="float",
        unit="load",
        description="5 minute load average"
    ),

    Metric(
        name="load_average_15m",
        query="node_load15",
        category="cpu",
        datatype="float",
        unit="load",
        description="15 minute load average"
    ),

    # ==============================================================
    # Memory
    # ==============================================================

    Metric(
        name="memory_used_percent",
        query="""
        (
        1 -
        (
        node_memory_MemAvailable_bytes
        /
        node_memory_MemTotal_bytes
        )
        ) * 100
        """,
        category="memory",
        datatype="float",
        unit="percent",
        description="Memory usage percentage"
    ),

    Metric(
        name="memory_available_bytes",
        query="node_memory_MemAvailable_bytes",
        category="memory",
        datatype="float",
        unit="bytes",
        description="Available system memory"
    ),

    # ==============================================================
    # Disk
    # ==============================================================

    Metric(
        name="disk_used_percent",
        query="""
        (
        1 -
        (
        node_filesystem_avail_bytes{mountpoint="/"}
        /
        node_filesystem_size_bytes{mountpoint="/"}
        )
        ) * 100
        """,
        category="disk",
        datatype="float",
        unit="percent",
        description="Root filesystem usage"
    ),

    # ==============================================================
    # Network
    # ==============================================================

    Metric(
        name="network_receive_bytes_per_second",
        query='sum(rate(node_network_receive_bytes_total[1m]))',
        category="network",
        datatype="float",
        unit="bytes/sec",
        description="Incoming network throughput"
    ),

    Metric(
        name="network_transmit_bytes_per_second",
        query='sum(rate(node_network_transmit_bytes_total[1m]))',
        category="network",
        datatype="float",
        unit="bytes/sec",
        description="Outgoing network throughput"
    ),

    # ==============================================================
    # Security Exporter
    # ==============================================================

    Metric(
        name="active_user_sessions",
        query="active_user_sessions",
        category="security",
        datatype="integer",
        unit="count",
        description="Number of active logged in users"
    ),

    Metric(
        name="running_process_count",
        query="running_process_count",
        category="security",
        datatype="integer",
        unit="count",
        description="Number of running processes"
    ),

    Metric(
        name="listening_port_count",
        query="listening_port_count",
        category="security",
        datatype="integer",
        unit="count",
        description="Number of listening ports"
    ),

    Metric(
        name="failed_ssh_login_count",
        query="failed_ssh_login_count",
        category="security",
        datatype="integer",
        unit="count",
        description="Failed SSH login attempts"
    ),
]
