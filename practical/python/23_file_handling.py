"""
File Handling in Python:

Syntax:
    variable = open("file_name.extension", "mode")

Modes:
    'r'  - Read
    'w'  - Write (overwrites existing file or creates a new one)
    'a'  - Append (adds data to the end of the file)
    'r+' - Read and Write
"""

# --- Writing a new file (overwrites if it exists) ---
student_file = open('student.txt', 'w')
student_file.write('New student record file\n')
student_file.close()

# --- Appending to the existing file ---
student_file = open('student.txt', 'a')
student_file.write('Student age is 26\n')
student_file.close()

# --- Reading the file ---
student_file = open('student.txt', 'r')

# Check if file is readable
print("Is readable?", student_file.readable())  # Output: True

# Read entire content
print("\nFull content of the file:")
print(student_file.read())

student_file.close()

# --- Overwriting content with new data ---
student_file = open('student.txt', 'w')
student_file.write('Student name is Adan\n')
student_file.close()

# --- Reading specific line using readlines() ---
student_file = open('student.txt', 'r')
lines = student_file.readlines()
if len(lines) > 0:
    print("\nReading first line only:")
    print(lines[0])  # prints the first line (index 0)
student_file.close()
