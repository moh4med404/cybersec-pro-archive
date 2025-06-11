# Integer variable
age = 25  # The age of a person

# Float variable
height = 5.9  # Height in feet

# String variable
name = "Moha"  # Person's name

# Boolean variable
is_student = True  # Indicates whether the person is a student

# ---------- Using the Variables ----------

# Printing all variables with descriptions
print("Name:", name)
print("Age:", age)
print("Height (in feet):", height)
print("Is a student:", is_student)

# ---------- Updating Variables ----------

# Let's say Moha has a birthday
age = age + 1  # Increment age by 1
print("New age after birthday:", age)

# Moha graduates
is_student = False  # No longer a student
print("Is a student after graduation:", is_student)

# Multi-line comment: Rules for variable names in Python
"""
Rules for Variable Names in Python:

1. Variable names must begin with a letter (A-Z or a-z) or an underscore (_).
   Examples: name, _score, totalMarks

2. The rest of the name can contain letters, numbers, or underscores.
   Examples: user1, total_2, _temp_value

3. Variable names are case-sensitive.
   Example: 'Age' and 'age' are different variables.

4. You cannot use Python reserved keywords as variable names.
   Example: 'for', 'if', 'class', 'def', etc. are invalid variable names.

5. Variable names should be descriptive and follow naming conventions like snake_case.
   Example: first_name, user_score (preferred for readability)

Note: There is no need to declare a variable type explicitly in Python — it’s dynamically typed.
"""
