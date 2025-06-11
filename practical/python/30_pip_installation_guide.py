"""
30_pip_installation_guide.py

This script documents how to use pip, Python's package installer,
to manage external libraries not included in the standard library.
Use these commands in your terminal or command prompt.
"""

print("=== PIP PACKAGE MANAGEMENT GUIDE ===")

# -------------------------------
# 1. Installing Packages with pip
# -------------------------------

# Basic installation:
# pip install package_name

# Example:
# pip install requests
# → Installs the 'requests' library, commonly used to make HTTP requests.

# -------------------------------
# 2. Common Variants
# -------------------------------

# Install the latest version of a package:
# pip install somepackage

# Install a specific version:
# pip install somepackage==1.2.3

# Upgrade a package to the latest version:
# pip install --upgrade somepackage

# Uninstall a package:
# pip uninstall somepackage

# -------------------------------
# 3. Package Management Tools
# -------------------------------

# List all installed packages:
# pip list

# Freeze all installed packages and versions (for requirements file):
# pip freeze

# Save to requirements.txt:
# pip freeze > requirements.txt

# Install from a requirements file:
# pip install -r requirements.txt

# -------------------------------
# 4. Example: Using an Installed Package
# -------------------------------

# You must install 'requests' first using pip:
# pip install requests

# Then in your Python code:
# import requests
# response = requests.get("https://httpbin.org/get")
# print(response.status_code)
# print(response.json())

print("Use these pip commands in the terminal (not inside Python scripts).")
