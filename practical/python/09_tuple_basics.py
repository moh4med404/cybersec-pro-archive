"""
Tuple Basics in Python:

- Creating tuples
- Accessing elements
- Immutability (tuples cannot be changed after creation)
- Useful tuple operations
"""

# Creating tuples
t1 = (1, 2, 3, 4, 5)              # Tuple of integers
t2 = ('moha', 'adam', 'dau')      # Tuple of strings
t3 = (9, 'september', 29.5)       # Mixed data types tuple
t4 = (1,)                         # Single element tuple (note the comma)

print("t1:", t1)
print("t2:", t2)
print("t3:", t3)
print("t4 (single element):", t4)

# Accessing elements by index (0-based)
print("t1[0]:", t1[0])           # 1
print("t2[-1]:", t2[-1])         # 'dau'

# Tuples are immutable - cannot add, remove or change elements
# The following operations will raise errors:
# t1[0] = 10           # TypeError: 'tuple' object does not support item assignment
# t1.append(6)         # AttributeError: 'tuple' object has no attribute 'append'

# You can use slicing on tuples
print("t1 slice (1 to 3):", t1[1:4])  # (2, 3, 4)

# Tuple concatenation
t5 = t1 + t2
print("Concatenated tuple:", t5)

# Tuple repetition
t6 = t2 * 2
print("Repeated tuple:", t6)

# Tuple unpacking
a, b, c = (10, 20, 30)
print("Unpacked values:", a, b, c)

# Useful functions with tuples
print("Length of t1:", len(t1))
print("Max value in t1:", max(t1))
print("Min value in t1:", min(t1))
print("Index of 3 in t1:", t1.index(3))
print("Count of 2 in t1:", t1.count(2))
