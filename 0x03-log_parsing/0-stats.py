#!/usr/bin/python3
import sys
import re

# regular expression to match expected input format
pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) - \[(?P<date>[^\]]+)\] '
    r'"GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)'
)

total_size = 0
status_count = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0


# defining printing funct
def print_stats():
    """"
    Function to print statistics
    """
    print(f'File size: {total_size}')
    for status in sorted(status_count.keys()):
        if status_count[status] > 0:
            print(f'{status}: {status_count[status]}')


try:
    for line in sys.stdin:
        match = pattern.match(line)
        if match:
            status_code = match.group('status')
            file_size = int(match.group('size'))

            total_size += file_size

            if status_code in status_count:
                status_count[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
finally:
    print_stats()
