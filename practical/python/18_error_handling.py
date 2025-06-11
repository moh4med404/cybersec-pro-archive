"""
Error Handling in Python:

- try: Run code that might raise an exception.
- except: Handle the exception.
- else: Run only if no exception occurs.
- finally: Always runs, used for cleanup tasks.
"""

# try + except
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number.")

print()

# try + except + else
try:
    number = int(input("Enter another number: "))
except ValueError:
    print("That's not a valid number.")
else:
    print(f"You entered: {number}")

print()

# try + except + finally
try:
    number = int(input("Enter yet another number: "))
except ValueError:
    print("That's not a valid number.")
finally:
    print("Input attempt finished.")

print()

# Full structure: try + except + else + finally
try:
    number = int(input("Enter a number to divide 10 by: "))
    result = 10 / number
except ValueError:
    print("Invalid input! Not a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result is: {result}")
finally:
    print("Done with operation.")

print()

# Raising a built-in exception manually
age = int(input("Enter your age: "))
if age < 0:
    raise ValueError("Age cannot be negative!")

print()

# Custom exception class
class NegativeAgeError(Exception):
    """Custom exception for negative ages."""
    pass

# Raising and handling a custom exception
try:
    age = int(input("Enter your age again: "))
    if age < 0:
        raise NegativeAgeError("Custom: Age cannot be negative!")
except NegativeAgeError as e:
    print(f"Caught error: {e}")
