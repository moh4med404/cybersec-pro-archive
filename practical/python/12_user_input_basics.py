"""
User Input in Python:

- input() reads input as a string by default
- You can convert input to int, float, etc. using type casting
"""

# Reading a string input
name = input("Enter your name: ")
print("Hello,", name)

# Reading an integer input
age = int(input("Enter your age: "))
print("You are", age, "years old.")

# Reading a float input
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters.")

# Reading multiple values in one line (space-separated)
# Example input: 10 20
x, y = input("Enter two numbers separated by space: ").split()
print("x =", x)
print("y =", y)

# Reading and converting to int in one line
a, b = map(int, input("Enter two integers separated by space: ").split())
print("Sum of a and b:", a + b)
