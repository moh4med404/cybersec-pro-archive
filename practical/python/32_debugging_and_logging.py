"""
34_debugging_and_logging.py

This script demonstrates basic debugging techniques and logging usage in Python.
"""

# -------------------------------
# 1. Debugging with print()
# -------------------------------
def divide(a, b):
    print("DEBUG: a =", a)
    print("DEBUG: b =", b)
    if b == 0:
        print("ERROR: Cannot divide by zero!")
        return None
    return a / b

result = divide(10, 2)
print("Result:", result)

# -------------------------------
# 2. Using the built-in debugger (pdb)
# -------------------------------
# Uncomment the following lines to try it

# import pdb
# a, b = 5, 0
# pdb.set_trace()  # This will start the interactive debugger
# result = divide(a, b)

# -------------------------------
# 3. Using the logging module (Recommended for real projects)
# -------------------------------
import logging

# Configure the logging system
logging.basicConfig(
    level=logging.DEBUG,               # Set the minimum logging level
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
    filename='app.log',                # Log file (optional)
    filemode='w'                       # Overwrite log file each run
)

def safe_divide(a, b):
    logging.debug(f"Trying to divide {a} by {b}")
    if b == 0:
        logging.error("Attempted to divide by zero")
        return None
    return a / b

x = 10
y = 0
logging.info("Starting division operation")
result = safe_divide(x, y)
logging.info(f"Result: {result}")

# -------------------------------
# 4. Logging Levels Overview
# -------------------------------
# logging.debug("Debugging info")      # Detailed info for developers
# logging.info("General info")         # Routine messages
# logging.warning("Something odd")     # Caution messages
# logging.error("Major problem")       # Serious issue
# logging.critical("System failure")   # Critical failure

print("Check 'app.log' file for full logging output.")
