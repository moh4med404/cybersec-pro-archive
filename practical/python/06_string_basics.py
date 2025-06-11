"""
Simple String Basics in Python
"""

# Create a string
s = "Hello, World!"
print(s)

# Lowercase
print(s.lower())  # hello, world!

# Uppercase
print(s.upper())  # HELLO, WORLD!

# Strip spaces
s2 = "  hi  "
print(s2.strip())  # hi

# Replace substring
print(s.replace("World", "Moha"))  # Hello, Moha!

# Split string by comma
print("a,b,c".split(','))  # ['a', 'b', 'c']

# Join list with '--'
print('--'.join(['a', 'b']))  # a--b

# Find first 'l'
print(s.find('l'))  # 2

# Indexing and slicing
word = "CyberSec"
print(word[0])     # C
print(word[-1])    # c
print(word[1:4])   # ybe
print(word[:])     # CyberSec

# String formatting
name = "Alice"
age = 30
print(f"My name is {name} and I'm {age}")
print("My name is {} and I'm {}".format(name, age))

# Check string content
s3 = "admin123"
print(s3.isdigit())     # False
print(s3.isalpha())     # False
print(s3.isalnum())     # True
print(s3.startswith("adm"))  # True
print(s3.endswith("123"))    # True
