"""
33_importing_modules.py

This script explains various ways to import modules in Python,
including built-in, third-party, and custom modules.
"""

# -------------------------------
# 1. Import the Whole Module
# -------------------------------
import math
print("Square root of 16:", math.sqrt(16))  # Output: 4.0

# -------------------------------
# 2. Import with an Alias
# -------------------------------
import numpy as np
print("Numpy array:", np.array([1, 2, 3]))  # Output: [1 2 3]

# -------------------------------
# 3. Import Specific Functions or Variables
# -------------------------------
from math import sqrt, pi
print("Square root of 25:", sqrt(25))       # Output: 5.0
print("Value of pi:", pi)                   # Output: 3.141592653589793

# -------------------------------
# 4. Import All Names (Not Recommended)
# -------------------------------
from math import *
print("Sin of π/2:", sin(pi / 2))           # Output: 1.0
# Note: This is discouraged in larger scripts due to possible name conflicts.

# -------------------------------
# 5. Importing Your Own Python Files (Modules)
# -------------------------------
# Suppose you have two files in the same directory:
#  - calc.py (contains functions)
#  - main.py (this script, importing calc)

# --- calc.py ---
# def add(a, b):
#     return a + b
#
# def sub(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b

# --- main.py ---
# from calc import *
# a, b = 1, 2
# c = add(a, b)
# print("Result of add:", c)

# -------------------------------
# 6. Commonly Used Built-in Modules
# -------------------------------
import os       # For interacting with the operating system
import sys      # For accessing system-specific parameters and functions
import time     # For handling time-related tasks
import random   # For generating random numbers

print("Current working directory:", os.getcwd())
print("Random number between 1 and 10:", random.randint(1, 10))
print("Sleeping for 1 second...")
time.sleep(1)
print("Python executable path:", sys.executable)
