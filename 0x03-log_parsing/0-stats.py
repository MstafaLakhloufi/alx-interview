#!/usr/bin/python3
import sys
import signal
from collections import defaultdict

# Initialize variables to track metrics
status_codes = defaultdict(int)
total_file_size = 0
line_count = 0

# Function to handle printing of statistics
def print_stats():
    global total_file_size
    print(f"File size: {total_file_size}")
    for status in sorted(status_codes.keys()):
        print(f"{status}: {status_codes[status]}")

# Signal handler for keyboard interrupt (CTRL + C)
def handle_interrupt(signal, frame):
    print_stats()
    sys.exit(0)

# Register the interrupt signal
signal.signal(signal.SIGINT, handle_interrupt)

# Process stdin line by line
for line in sys.stdin:
    parts = line.split()
    
    # Skip lines that don't match the expected format
    if len(parts) < 7:
        continue

    ip_address, date, status_code, file_size = parts[0], parts[3], parts[5], parts[6]
    
    try:
        # Extract status code and file size
        status_code = int(status_code)
        file_size = int(file_size)
        
        # Check if the status code is one of the valid codes
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            status_codes[status_code] += 1
            total_file_size += file_size
    except ValueError:
        # If parsing the status code or file size fails, ignore the line
        continue

    line_count += 1
    
    # After every 10 lines, print stats
    if line_count % 10 == 0:
        print_stats()