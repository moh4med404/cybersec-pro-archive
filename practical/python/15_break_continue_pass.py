"""
Loop Control Statements in Python:

- break    : Exit the loop completely
- continue : Skip the rest of the current loop iteration
- pass     : Do nothing (used as a placeholder)
"""

# break example: stop the loop when number is 3
print("BREAK example:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)
print("Loop exited with break\n")

# continue example: skip number 3
print("CONTINUE example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
print("Loop skipped 3 using continue\n")

# pass example: used as a placeholder
print("PASS example:")
for i in range(1, 4):
    if i == 2:
        pass  # does nothing
    print("Processing:", i)
