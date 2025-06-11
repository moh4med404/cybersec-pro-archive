"""
Type Conversion in Python:

1. Implicit Conversion (Automatic)
2. Explicit Conversion (Manual using functions like int(), float(), str(), etc.)
"""

# Implicit Type Conversion
x = 10      # int
y = 3.5     # float
z = x + y   # int + float -> float automatically
print(z)            # 13.5
print(type(z))      # <class 'float'>

# Explicit Type Conversion (Type Casting)

# String to int
a = "123"
b = int(a)
print(b, type(b))   # 123 <class 'int'>

# Float to int (decimal part truncated)
c = int(4.99)
print(c)            # 4

# Int to string
d = str(100)
print(d, type(d))   # '100' <class 'str'>

# String to list (each character becomes an element)
e = list("hello")
print(e)            # ['h', 'e', 'l', 'l', 'o']

# Additional examples:

# Bool conversion
print(bool(0))      # False
print(bool(5))      # True

# List to tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)     # (1, 2, 3)

# Tuple to set (removes duplicates)
my_tuple2 = (1, 2, 2, 3)
my_set = set(my_tuple2)
print(my_set)       # {1, 2, 3}
