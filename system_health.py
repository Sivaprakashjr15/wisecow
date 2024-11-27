import psutil
import logging
import time

# Configure logging
logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage
PROCESS_THRESHOLD = 200  # number of processes

def monitor_system_health():
    # Get system metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    disk = psutil.disk_usage("/")
    disk_usage = disk.percent
    process_count = len(psutil.pids())

    # Log system metrics
    logging.info(f"CPU Usage: {cpu_usage}%")
    logging.info(f"Memory Usage: {memory_usage}%")
    logging.info(f"Disk Usage: {disk_usage}%")
    logging.info(f"Process Count: {process_count}")

    # Check thresholds
    if cpu_usage > CPU_THRESHOLD:
        alert(f"High CPU Usage: {cpu_usage}% (Threshold: {CPU_THRESHOLD}%)")

    if memory_usage > MEMORY_THRESHOLD:
        alert(f"High Memory Usage: {memory_usage}% (Threshold: {MEMORY_THRESHOLD}%)")

    if disk_usage > DISK_THRESHOLD:
        alert(f"High Disk Usage: {disk_usage}% (Threshold: {DISK_THRESHOLD}%)")

    if process_count > PROCESS_THRESHOLD:
        alert(f"High Process Count: {process_count} (Threshold: {PROCESS_THRESHOLD})")


def alert(message):
    # Print alert to console
    print(f"ALERT: {message}")
    # Log alert to file
    logging.warning(message)


if __name__ == "__main__":
    print("Starting system health monitor...")
    logging.info("System health monitor started.")
    
    # Run the monitor every 10 seconds
    try:
        while True:
            monitor_system_health()
            time.sleep(10)
    except KeyboardInterrupt:
        print("System health monitor stopped.")
        logging.info("System health monitor stopped.")
