"""
While Loops in Python:

- A while loop repeats as long as the condition is True
- You can nest one while loop inside another
"""

# Basic while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

print("Finished basic while loop\n")

# Nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i = {i}, j = {j}")
        j += 1
    i += 1

print("Finished nested while loop")
