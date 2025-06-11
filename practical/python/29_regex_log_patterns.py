import re

# ------------------------------------------------------------
# Example 1: Match Email Addresses
# ------------------------------------------------------------
log1 = "User test@example.com failed to login from 192.168.1.5"

# Regex pattern to match email addresses
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

email_match = re.search(email_pattern, log1)
if email_match:
    print("Found email:", email_match.group())
else:
    print("No email found.")

# ------------------------------------------------------------
# Example 2: Match URLs (Useful for phishing detection)
# ------------------------------------------------------------
log2 = "Malicious link: http://bad.com/path?query=123"

# Regex pattern to match URLs (http and https)
url_pattern = r"http[s]?://[^\s<>\"']+"

url_matches = re.findall(url_pattern, log2)
print("Found URLs:", url_matches)  # Output: ['http://bad.com/path?query=123']

# ------------------------------------------------------------
# Example 3: Match Timestamps in logs (YYYY-MM-DD HH:MM:SS)
# ------------------------------------------------------------
log3 = "Login failed at 2025-05-06 14:22:01 from 10.0.0.2"

# Regex pattern to match timestamps
timestamp_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

timestamp_match = re.search(timestamp_pattern, log3)
if timestamp_match:
    print("Found timestamp:", timestamp_match.group())
else:
    print("No timestamp found.")

# ------------------------------------------------------------
# Example 4: Match HTTP Methods (GET, POST, etc.)
# ------------------------------------------------------------
http_request = "POST /login HTTP/1.1"

# Regex to extract common HTTP methods
http_method_pattern = r"\b(GET|POST|PUT|DELETE|HEAD|OPTIONS)\b"

method_match = re.search(http_method_pattern, http_request)
if method_match:
    print("Found HTTP method:", method_match.group())
else:
    print("No HTTP method found.")

# ------------------------------------------------------------
# Example 5: Match Failed Login Attempts and Extract IP
# ------------------------------------------------------------
log5 = "ERROR: Failed password for invalid user root from 192.168.0.101"

# Regex pattern to extract IP address from failed login attempts
# \b\d{1,3}(\.\d{1,3}){3}\b matches an IPv4 address
failed_login_pattern = r"Failed password for .* from (\b\d{1,3}(?:\.\d{1,3}){3}\b)"

failed_login_match = re.search(failed_login_pattern, log5)
if failed_login_match:
    print("Failed login from IP:", failed_login_match.group(1))
else:
    print("No failed login IP found.")
