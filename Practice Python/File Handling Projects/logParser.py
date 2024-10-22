# Log Parser: Write a program to read log files (like .txt or .csv) and extract meaningful information (e.g., errors, specific user data).

import re
from collections import defaultdict

# 127.0.0.1 - - [21/Oct/2024:10:23:01 +0000] "GET /index.html HTTP/1.1" 200 2326


# Define a regex pattern for parsing a common log format (e.g., Apache)
log_pattern = re.compile(
    r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP address
    r' - - '  # Literal match
    r'\[(?P<datetime>[^\]]+)\]'  # Date and time
    r' "(?P<method>\w+) (?P<url>[^\s]+) [^"]+"'  # HTTP Method and URL
    r' (?P<status>\d{3})'  # HTTP status code
    r' (?P<size>\d+)'  # Size of the response
)

def par_log_line(line):
    """
    Parsing a log line and return in dictionary
    """

    match = log_pattern.match(line)
    if match:
        return match.groupdict()
    return None