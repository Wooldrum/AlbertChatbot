# ========================================
# Dependency Checker and Installer
# ========================================

import os
import re
import sys
import subprocess

# Output file for required libraries
output_file = "PiP-Downloads.txt"

def extract_imports(file_path):
    """
    Extract all imported libraries from a given Python file.
    """
    imports = set()
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                # Match 'import library' or 'from library import ...'
                match = re.match(r'^\s*(import|from) ([\w\.]+)', line)
                if match:
                    imports.add(match.group(2).split('.')[0])  # Only take the top-level package
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return imports

def scan_for_dependencies(base_dir):
    """
    Scan all Python files in the base directory for imported libraries.
    """
    dependencies = set()
    for filename in os.listdir(base_dir):
        if filename.endswith(".py") and filename != os.path.basename(__file__):
            file_path = os.path.join(base_dir, filename)
            print(f"Scanning file: {file_path}")
            dependencies.update(extract_imports(file_path))
    return dependencies

def write_dependencies_to_file(dependencies, base_dir):
    """
    Write the list of dependencies to PiP-Downloads.txt.
    """
    output_path = os.path.join(base_dir, output_file)
    try:
        with open(output_path, "w") as f:
            if dependencies:
                f.write("\n".join(sorted(dependencies)))
                print(f"Dependencies written to {output_file}: {sorted(dependencies)}")
            else:
                f.write("No non-standard dependencies found.")
                print(f"No non-standard dependencies found. {output_file} is empty.")
    except Exception as e:
        print(f"Error writing dependencies to file: {e}")

def install_dependencies(dependencies):
    """
    Install the dependencies using pip in subprocesses.
    """
    for dependency in dependencies:
        try:
            print(f"Installing: {dependency}")
            subprocess.run([sys.executable, "-m", "pip", "install", dependency], check=True)
            print(f"Successfully installed: {dependency}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {dependency}: {e}")
        except Exception as e:
            print(f"Unexpected error installing {dependency}: {e}")

def generate_pip_downloads(base_dir):
    """
    Generate the PiP-Downloads.txt file with non-standard library dependencies
    and attempt to install them.
    """
    try:
        print("Scanning for dependencies...")
        all_imports = scan_for_dependencies(base_dir)
        
        # Write to the output file
        write_dependencies_to_file(all_imports, base_dir)
        
        # Attempt to install the dependencies
        if all_imports:
            print("Attempting to install dependencies...")
            install_dependencies(all_imports)
    except Exception as e:
        print(f"Error generating dependencies: {e}")

if __name__ == "__main__":
    try:
        base_directory = os.path.dirname(os.path.abspath(__file__))
        generate_pip_downloads(base_directory)
        print(f"\nDependency check and installation complete. Results saved to '{output_file}'.")
        input("\nPress Enter to exit...")
    except Exception as e:
        print(f"Unexpected error: {e}")
        input("\nPress Enter to exit...")
