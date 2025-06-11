"""
List Basics in Python:

- Creating lists with different data types
- Accessing elements by index
- Combining lists
- Adding/removing elements
- Useful list methods
"""

# Creating lists
A = [1, 2, 3, 4, 5]               # Integer list
B = ['moha', 'adam', 'dau']       # String list
C = [9, 'september', 29.5]        # Mixed data types list

# Accessing element by index (0-based)
print("A[0]:", A[0])              # Output: 1

# Combining two lists into a new list
D = A + B
print("Combined list D:", D)

# Adding elements
A.append(7)                       # Adds 7 at the end: [1,2,3,4,5,7]
print("After append:", A)

A.insert(5, 6)                   # Insert 6 at index 5: [1,2,3,4,5,6,7]
print("After insert:", A)

# Removing elements
A.remove(1)                     # Removes the first occurrence of value 1
print("After remove(1):", A)

removed_value = A.pop(2)        # Removes element at index 2 (third element)
print(f"After pop(2): {A}, removed value: {removed_value}")

removed_last = A.pop()          # Removes last element
print(f"After pop(): {A}, removed last value: {removed_last}")

# Extending list with multiple values
A.extend([0, 1, 10, 11])        # Adds multiple elements at the end
print("After extend:", A)

# Useful functions on list
print("Min value:", min(A))     # Minimum value
print("Max value:", max(A))     # Maximum value
print("Sum of values:", sum(A)) # Sum of values

# Sorting the list
A.sort()
print("Sorted list:", A)

# Reversing the list
A.reverse()
print("Reversed list:", A)

# Copying the list
new_list = A.copy()
print("Copied list:", new_list)

# Additional useful list methods

# Count occurrences of a value
count_1 = A.count(1)
print("Count of 1 in list:", count_1)

# Find index of a value
index_10 = A.index(10)
print("Index of 10:", index_10)

# Clear all elements
new_list.clear()
print("Cleared copied list:", new_list)
