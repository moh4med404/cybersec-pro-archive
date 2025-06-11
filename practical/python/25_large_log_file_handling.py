"""
25 - Handling Large Log Files in Python

Demonstrates:
- Reading large files line-by-line (memory-safe)
- Filtering log entries (e.g., lines with "ERROR")
- Writing filtered results to a new file
- Counting specific events (e.g., failed logins)
- Using generators for efficient streaming
- Reading compressed .gz log files
"""

import gzip

# --- 1. Reading large file line-by-line ---
print("🔹 Reading lines from server.log:")
try:
    with open("server.log", "r") as log_file:
        for line in log_file:
            print(line.strip())  # .strip() removes \n
except FileNotFoundError:
    print("File server.log not found. (Skip demo)")

# --- 2. Filtering lines with "ERROR" ---
print("\n🔹 Filtering lines containing 'ERROR':")
try:
    with open("server.log", "r") as log_file:
        for line in log_file:
            if "ERROR" in line:
                print(line.strip())
except FileNotFoundError:
    print("File server.log not found. (Skip demo)")

# --- 3. Writing filtered lines to a new file ---
print("\n🔹 Writing 'ERROR' lines to errors.log:")
try:
    with open("server.log", "r") as source, open("errors.log", "w") as target:
        for line in source:
            if "ERROR" in line:
                target.write(line)
    print("Filtered errors written to errors.log")
except FileNotFoundError:
    print("File server.log not found. (Skip write demo)")

# --- 4. Count failed logins in auth.log ---
print("\n🔹 Counting 'Failed password' entries in auth.log:")
count = 0
try:
    with open("auth.log", "r") as log_file:
        for line in log_file:
            if "Failed password" in line:
                count += 1
    print(f"❗ Failed logins found: {count}")
except FileNotFoundError:
    print("File auth.log not found. (Skip count)")

# --- 5. Generator to process only 'ERROR' lines ---
print("\n🔹 Using generator to yield 'ERROR' lines:")
def error_lines(filepath):
    try:
        with open(filepath, "r") as f:
            for line in f:
                if "ERROR" in line:
                    yield line
    except FileNotFoundError:
        yield from []

for error in error_lines("server.log"):
    print("Generator:", error.strip())

# --- 6. Reading from gzipped .log.gz file ---
print("\n🔹 Reading compressed server.log.gz for 'ERROR' lines:")
try:
    with gzip.open("server.log.gz", "rt") as log_file:
        for line in log_file:
            if "ERROR" in line:
                print("GZ:", line.strip())
except FileNotFoundError:
    print("File server.log.gz not found. (Skip gzip demo)")
