import os
import re
import subprocess


def scan_dependencies(directory):
    """
    Scans all Python files in the given directory for import statements and returns a set of dependencies.
    """
    dependencies = set()

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        # Match import and from-import statements
                        matches = re.findall(r"^(?:from\s+(\S+)|import\s+(\S+))", content, re.MULTILINE)
                        for match in matches:
                            module = match[0] or match[1]
                            if module:  # Avoid empty matches
                                dependencies.add(module.split('.')[0])
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

    # Special case for spaCy models
    if "spacy" in dependencies:
        dependencies.add("spacy-model-en_core_web_sm")

    return dependencies


def install_dependencies(dependencies):
    """
    Attempts to install the listed dependencies via pip. Handles spaCy models separately.
    """
    failed_dependencies = []

    for dependency in dependencies:
        if dependency == "spacy-model-en_core_web_sm":
            # Special handling for spaCy models
            try:
                print("Downloading spaCy model 'en_core_web_sm'...")
                subprocess.check_call(["python", "-m", "spacy", "download", "en_core_web_sm"])
            except Exception as e:
                print(f"Failed to download spaCy model: {e}")
                failed_dependencies.append("en_core_web_sm (manual installation required)")
        else:
            try:
                print(f"Installing {dependency}...")
                subprocess.check_call(["pip", "install", dependency])
            except Exception as e:
                print(f"Failed to install {dependency}: {e}")
                failed_dependencies.append(dependency)

    return failed_dependencies


def generate_pip_downloads(dependencies, output_file="PiP-Downloads.txt"):
    """
    Saves dependencies to a text file for manual installation.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for dependency in dependencies:
                if dependency == "spacy-model-en_core_web_sm":
                    f.write("# spaCy model required: en_core_web_sm\n")
                    f.write("python -m spacy download en_core_web_sm\n")
                else:
                    f.write(f"{dependency}\n")
        print(f"Dependencies saved to {output_file}.")
    except Exception as e:
        print(f"Failed to save dependencies to {output_file}: {e}")


if __name__ == "__main__":
    print("Scanning for dependencies...")
    dependencies = scan_dependencies(os.getcwd())

    print(f"Dependencies found: {dependencies}")

    # Attempt to install dependencies
    failed_dependencies = install_dependencies(dependencies)

    # Save dependencies to a file
    generate_pip_downloads(dependencies)

    if failed_dependencies:
        print("The following dependencies could not be installed automatically:")
        for dep in failed_dependencies:
            print(f"- {dep}")

    print("Dependency check complete.")
    input("Press Enter to exit...")
