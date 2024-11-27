import re
from collections import Counter

def parse_log(log_file):
    # Regular expression to match typical Apache/Nginx log format
    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<method>\w+) (?P<url>.*?) HTTP/\d+\.\d+" (?P<status>\d+) (?P<size>\d+|-)'
    )
    
    # Data containers
    requests = []
    errors_404 = []
    ip_addresses = []

    with open(log_file, 'r') as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                ip_addresses.append(match.group("ip"))
                requests.append(match.group("url"))
                if match.group("status") == "404":
                    errors_404.append(match.group("url"))
    
    return requests, errors_404, ip_addresses


def analyze_logs(log_file):
    requests, errors_404, ip_addresses = parse_log(log_file)
    
    # Count occurrences
    most_requested_pages = Counter(requests).most_common(10)
    most_frequent_ips = Counter(ip_addresses).most_common(10)
    total_404_errors = len(errors_404)
    
    # Print summarized report
    print("\n--- Log Analysis Report ---")
    print(f"Total 404 Errors: {total_404_errors}")
    print("\nMost Requested Pages:")
    for url, count in most_requested_pages:
        print(f"{url}: {count} requests")
    
    print("\nIP Addresses with the Most Requests:")
    for ip, count in most_frequent_ips:
        print(f"{ip}: {count} requests")


if __name__ == "__main__":
    # Provide the log file name
    log_file_path = "access.log"  # Replace with the path to your log file
    analyze_logs(log_file_path)
