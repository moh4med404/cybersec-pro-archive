"""
36_script_structure_best_practices.py

A guide on organizing Python scripts effectively and applying best coding practices.
"""

# -------------------------------
# 1. Use a Main Function
# -------------------------------
def main():
    """
    Main function where the script execution begins.
    Keeps code organized and prevents unwanted runs when importing.
    """
    print("Hello! This is the main program.")

# -------------------------------
# 2. Use the if __name__ == "__main__" Guard
# -------------------------------
# Ensures main() runs only when script is executed directly, not when imported.
if __name__ == "__main__":
    main()

# -------------------------------
# 3. Modularize Your Code
# -------------------------------
# Break large scripts into functions and classes for readability and reuse.

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b

# -------------------------------
# 4. Use Meaningful Variable and Function Names
# -------------------------------
# Names should be descriptive to make the code self-documenting.

result = add(10, 5)
print(f"Adding 10 and 5 gives {result}")

# -------------------------------
# 5. Follow PEP 8 Style Guidelines
# -------------------------------
# - Use 4 spaces per indentation level
# - Limit lines to 79 characters
# - Use lowercase_with_underscores for functions and variables
# - Use CapitalizedWords for classes

# -------------------------------
# 6. Add Comments and Docstrings
# -------------------------------
# Explain why something is done, not just what.
# Docstrings for modules, functions, classes help documentation tools.

def multiply(a, b):
    """
    Multiply two numbers and return the result.

    Parameters:
    a (int or float): first number
    b (int or float): second number

    Returns:
    int or float: product of a and b
    """
    return a * b

# -------------------------------
# 7. Handle Exceptions Gracefully
# -------------------------------
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# -------------------------------
# 8. Avoid Hardcoding Values
# -------------------------------
# Use constants or config files for values that might change.

MAX_RETRIES = 3

for attempt in range(MAX_RETRIES):
    print(f"Attempt {attempt + 1}")

# -------------------------------
# 9. Keep Scripts Small and Focused
# -------------------------------
# If a script grows large, split it into modules and packages.

# -------------------------------
# 10. Use Logging Instead of print() for Larger Projects
# -------------------------------
import logging

logging.basicConfig(level=logging.INFO)
logging.info("This is an informational message.")

# -------------------------------
# Summary
# -------------------------------
"""
- Always use a main() function with the if __name__ == "__main__" guard.
- Modularize code into reusable functions/classes.
- Write clear, descriptive names and comments.
- Follow PEP 8 style guide.
- Handle errors with try/except.
- Use constants or configuration.
- Use logging for better runtime info.
"""

