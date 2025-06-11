"""
Function Basics in Python:

- Defining and calling functions
- Parameters and return values
- Default parameters, keyword arguments
- *args and **kwargs
- Functions calling other functions
"""

# 1) Defining and Calling Functions
def greet():
    print("Hello, world!")

greet()  # Calling the function


# 2) Function with Parameters
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")


# 3) Function with Return Value (No Parameters)
def get_greeting():
    return "Hello, world!"

message = get_greeting()
print(message)


# 4) Function with Parameters and Return Value
def add(a, b):
    return a + b

result = add(5, 3)
print("Addition Result:", result)


# 5) Multiple Parameters and Multiple Return Values
def calculate(a, b):
    sum_ = a + b
    diff = a - b
    return sum_, diff

s, d = calculate(10, 4)
print("Sum:", s)
print("Difference:", d)


# 6) Default Parameter Values
def greet_default(name="Guest"):
    print(f"Hello, {name}!")

greet_default()         # Uses default
greet_default("Sam")    # Overrides default


# 7) Keyword Arguments
def introduce(name, age):
    print(f"{name} is {age} years old.")

introduce(age=25, name="John")  # Using keyword arguments


# 8) Variable Number of Arguments
# *args – accepts multiple positional arguments
def total(*args):
    return sum(args)

print("Total sum:", total(1, 2, 3, 4))


# **kwargs – accepts multiple keyword arguments
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30)


# 9) Functions Calling Other Functions
def square(x):
    return x * x

def double_square(y):
    return 2 * square(y)

print("Double square of 3:", double_square(3))
