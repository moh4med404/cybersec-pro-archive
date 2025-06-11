"""
24 - Working with File Paths using pathlib

Demonstrates:
- Creating and checking file paths
- Reading/writing/appending files
- Creating folders
- Writing a report file
- Finding files
"""

from pathlib import Path

# 1. Define file and folder paths
file_path = Path("data/example.txt")
folder_path = Path("data/logs")

# 2. Check if the file exists
if file_path.exists():
    print("✅ The file exists.")
else:
    print("❌ The file does NOT exist.")

# 3. Check if it's a file or directory
if file_path.is_file():
    print("📄 It's a file.")
if folder_path.is_dir():
    print("📁 It's a folder.")

# 4. Append to the file (if it exists)
if file_path.exists():
    with file_path.open("a") as f:
        f.write("\nAnother line added using pathlib + open()")

# 5. Extract file details
print("\n📂 File Info:")
print(" - File name     :", file_path.name)
print(" - Name only     :", file_path.stem)
print(" - Extension     :", file_path.suffix)
print(" - Parent folder :", file_path.parent)

# 6. Find .log files in the logs folder
print("\n🔍 .log files in 'data/logs':")
for log_file in folder_path.glob("*.log"):
    print(" -", log_file)

# 7. Find all .log files recursively
print("\n🔍 .log files (recursive):")
for log_file in folder_path.rglob("*.log"):
    print(" -", log_file)

# 8. Create a new folder for reports
new_folder = Path("output/reports")
new_folder.mkdir(parents=True, exist_ok=True)
print("\n✅ Folder created:", new_folder)

# 9. Write a report file into the new folder
report_file = new_folder / "report.txt"
with report_file.open("w") as report:
    report.write("CyberSec Python File Handling Report\n")
    report.write("Status: File and folder operations tested successfully.\n")

print("📝 Report written to:", report_file)

# ✅ We are not deleting the folder now, so it will remain with the report file.
