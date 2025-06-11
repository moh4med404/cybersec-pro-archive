import os
import sys
import subprocess

def list_files_in_directory():
    """List files and directories in the current working directory."""
    print("=== Current Working Directory ===")
    cwd = os.getcwd()
    print(f"Current directory: {cwd}")
    
    # List all files and directories
    print("Files and directories:")
    for item in os.listdir(cwd):
        print(f"- {item}")
    
def create_and_remove_directory():
    """Create and remove a directory."""
    new_dir = "test_directory"
    
    print("\n=== Creating and Removing a Directory ===")
    
    # Create a new directory
    try:
        os.mkdir(new_dir)
        print(f"Created new directory: {new_dir}")
    except FileExistsError:
        print(f"Directory {new_dir} already exists.")
    
    # Remove the directory
    os.rmdir(new_dir)
    print(f"Removed directory: {new_dir}")

def run_shell_command():
    """Run a shell command using subprocess."""
    print("\n=== Running Shell Command: Echo Hello World ===")
    
    try:
        # For Windows, use cmd.exe to run the echo command
        if sys.platform == "win32":
            result = subprocess.run(["cmd", "/c", "echo Hello, World!"], capture_output=True, text=True, check=True)
        else:
            # For Unix-like systems (Linux/macOS), directly run echo
            result = subprocess.run(["echo", "Hello, World!"], capture_output=True, text=True, check=True)
        
        print(f"Command Output: {result.stdout.strip()}")
    
    except subprocess.CalledProcessError as e:
        print(f"Error while running the command: {e}")
    except FileNotFoundError as e:
        print(f"File not found error: {e}")

def command_line_arguments():
    """Handle command-line arguments passed to the script."""
    print("\n=== Handling Command-Line Arguments ===")
    
    if len(sys.argv) > 1:
        print(f"Command-line arguments: {sys.argv[1:]}")
    else:
        print("No arguments provided.")

def main():
    """Main function to tie everything together."""
    list_files_in_directory()
    create_and_remove_directory()
    run_shell_command()
    command_line_arguments()

if __name__ == "__main__":
    main()
