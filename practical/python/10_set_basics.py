"""
Set Basics in Python:

- Creating sets
- Sets store unique elements (no duplicates)
- Unordered collection
- Common set operations
"""

# Creating sets
s1 = {1, 2, 3, 4, 5}           # Set of integers
s2 = {'moha', 'adam', 'dau'}   # Set of strings
s3 = set([9, 'september', 29.5])  # Using set() constructor with list

print("s1:", s1)
print("s2:", s2)
print("s3:", s3)

# Adding elements
s1.add(6)
print("After adding 6:", s1)

# Adding duplicates does nothing
s1.add(3)
print("After adding duplicate 3:", s1)

# Removing elements
s1.remove(4)  # Raises KeyError if 4 not in set
print("After removing 4:", s1)

s1.discard(10)  # Does not raise error if element not found
print("After discarding 10 (not present):", s1)

# Check membership
print("Is 5 in s1?", 5 in s1)  # True
print("Is 10 in s1?", 10 in s1) # False

# Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A:", A)
print("B:", B)

print("Union (A | B):", A | B)            # {1, 2, 3, 4, 5, 6}
print("Intersection (A & B):", A & B)     # {3, 4}
print("Difference (A - B):", A - B)       # {1, 2}
print("Symmetric Difference (A ^ B):", A ^ B)  # {1, 2, 5, 6}

# Set length
print("Length of A:", len(A))

# Clear all elements
A.clear()
print("After clearing A:", A)
