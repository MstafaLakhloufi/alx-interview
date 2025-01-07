#!/usr/bin/python3

import sys

def print_stats(file_size, status_codes):
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def main():
    file_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            # Check if the line matches the expected format
            if len(parts) >= 7 and parts[5][1:] == "GET" and parts[6] == "HTTP/1.1":
                try:
                    code = int(parts[8])  # status code
                    size = int(parts[9])  # file size
                    if code in status_codes:
                        status_codes[code] += 1
                        file_size += size
                except (ValueError, IndexError):
                    continue

            count += 1

            # Print statistics after every 10 lines or on keyboard interrupt
            if count % 10 == 0:
                print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        print_stats(file_size, status_codes)