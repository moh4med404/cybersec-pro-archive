"""
35_virtual_environments_venv.py

This guide explains how to create and use isolated Python environments
using the built-in `venv` module to manage dependencies per project.
"""

print("=== Virtual Environments with venv ===")

# -------------------------------------------------------
# 1. What is a Virtual Environment?
# -------------------------------------------------------
print("""
A virtual environment is a self-contained directory that contains a Python
installation for a particular version of Python, plus several additional
packages. It allows you to manage dependencies separately for different projects,
avoiding version conflicts and system-wide changes.
""")

# -------------------------------------------------------
# 2. Creating a Virtual Environment
# -------------------------------------------------------
print("""
To create a new virtual environment, open your terminal or command prompt and run:

  python -m venv myenv

This creates a folder named 'myenv' containing the isolated Python environment.
""")

# -------------------------------------------------------
# 3. Activating the Virtual Environment
# -------------------------------------------------------
print("""
Activate the environment to start using it.

- On Windows (Command Prompt):
    myenv\\Scripts\\activate.bat

- On Windows (PowerShell):
    myenv\\Scripts\\Activate.ps1

- On macOS/Linux:
    source myenv/bin/activate

After activation, your terminal prompt usually changes to show the active env.
""")

# -------------------------------------------------------
# 4. Installing Packages Inside Virtual Environment
# -------------------------------------------------------
print("""
Once activated, you can install packages using pip, and they will be
installed only in this environment:

  pip install requests

Use pip freeze > requirements.txt to save dependencies.
""")

# -------------------------------------------------------
# 5. Deactivating the Virtual Environment
# -------------------------------------------------------
print("""
To exit the virtual environment and go back to the system Python, run:

  deactivate
""")

# -------------------------------------------------------
# 6. Summary of Useful Commands
# -------------------------------------------------------
print("""
Summary:

# Create virtual environment:
python -m venv myenv

# Activate environment:
# Windows CMD:
myenv\\Scripts\\activate.bat
# Windows PowerShell:
myenv\\Scripts\\Activate.ps1
# macOS/Linux:
source myenv/bin/activate

# Install packages:
pip install package_name

# List installed packages:
pip list

# Save packages:
pip freeze > requirements.txt

# Deactivate environment:
deactivate
""")
