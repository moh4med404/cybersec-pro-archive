"""
Dictionary Basics in Python:

- Uses key-value pairs
- Keys must be unique and immutable
- Values can be any data type
"""

# Creating a dictionary
d = {'1': 'moha', '2': 'adan', '3': 'daud'}
print("Original dictionary d:", d)

# Accessing values
print("Get value for key '1':", d.get('1'))  # Output: moha

# Getting all keys and values
print("Keys:", d.keys())     # dict_keys(['1', '2', '3'])
print("Values:", d.values()) # dict_values(['moha', 'adan', 'daud'])

# Adding new key-value pair
d['4'] = 'ibrahim'
print("After adding key '4':", d)

# Overwriting an existing key's value
d['2'] = 'ahmed'
print("After overwriting key '2':", d)

# Deleting items
del d['3']                # Method 1: del
print("After del '3':", d)

d.pop('4')                # Method 2: pop()
print("After pop '4':", d)

d['5'] = 'new'
d.popitem()               # Method 3: popitem()
print("After popitem():", d)

# Copying a dictionary
copy_d = d.copy()
print("Copied dictionary:", copy_d)

# Updating a dictionary
a = {1: 'mohamed', 2: 'adan'}
b = {1: 'mohamed', 3: 'daud'}
a.update(b)
print("After a.update(b):", a)

# Clearing a dictionary
copy_d.clear()
print("After clear:", copy_d)
