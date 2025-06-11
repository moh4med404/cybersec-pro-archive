import json

# Open the log file and read it line by line
with open("logs.json", "r") as log_file:
    for line in log_file:
        log = json.loads(line)  # Convert JSON string to dictionary
        if log["event"] == "failed_login":
            print(f"❌ Failed login by {log['user']} from IP: {log['ip']}")
