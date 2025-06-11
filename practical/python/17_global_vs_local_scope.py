"""
Variable Scope in Python:

- Local Variables: Defined inside a function, accessible only within that function.
- Global Variables: Defined outside any function, accessible anywhere.
- To modify a global variable inside a function, use the 'global' keyword.
"""

# ----- Local Variable Example -----
def greet():
    message = "Hello"  # Local variable
    print(message)

greet()
# print(message)  # ❌ This would raise a NameError (uncomment to test)


# ----- Global Variable Example -----
name = "Alice"  # Global variable

def greet_global():
    print("Hello", name)  # Accessing global variable

greet_global()


# ----- Modifying Global Variable Inside Function -----
count = 0  # Global variable

def increment():
    global count  # Tells Python to use the global 'count'
    count += 1

increment()
print("Global count after increment:", count)  # Output: 1
