from prometheus_client import start_http_server, Gauge
import psutil
import subprocess
import time

# -------------------------
# Prometheus Metrics
# -------------------------

active_user_sessions = Gauge(
    "active_user_sessions",
    "Number of logged-in user sessions"
)

running_process_count = Gauge(
    "running_process_count",
    "Number of running processes"
)

listening_port_count = Gauge(
    "listening_port_count",
    "Number of listening TCP/UDP ports"
)

failed_ssh_logins = Gauge(
    "failed_ssh_logins",
    "Number of failed SSH login attempts found in auth.log"
)

# -------------------------
# Metric Collection
# -------------------------

def get_active_sessions():
    try:
        return len(psutil.users())
    except Exception:
        return 0


def get_process_count():
    try:
        return len(psutil.pids())
    except Exception:
        return 0


def get_listening_ports():
    try:
        result = subprocess.run(
            ["ss", "-tuln"],
            capture_output=True,
            text=True
        )

        lines = result.stdout.strip().split("\n")

        if len(lines) <= 1:
            return 0

        return len(lines) - 1

    except Exception:
        return 0


def get_failed_ssh_logins():
    try:
        count = 0

        with open("/var/log/auth.log", "r") as logfile:
            for line in logfile:
                if "Failed password" in line:
                    count += 1

        return count

    except Exception:
        return 0


def collect_metrics():

    active_user_sessions.set(
        get_active_sessions()
    )

    running_process_count.set(
        get_process_count()
    )

    listening_port_count.set(
        get_listening_ports()
    )

    failed_ssh_logins.set(
        get_failed_ssh_logins()
    )


# -------------------------
# Main
# -------------------------

if __name__ == "__main__":

    start_http_server(8000)

    print("Security Exporter running on port 8000")

    while True:
        collect_metrics()
        time.sleep(15)
