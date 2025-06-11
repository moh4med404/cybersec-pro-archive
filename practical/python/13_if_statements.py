"""
If Statements in Python:

- if        : Run code if condition is true
- if-else   : Choose between two blocks
- nested if : if inside another if
"""

# Simple if
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")

# if-else
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Nested if
score = int(input("Enter your score (0–100): "))
if score >= 50:
    if score >= 90:
        print("Excellent!")
    elif score >= 70:
        print("Good job!")
    else:
        print("You passed.")
else:
    print("You failed.")
