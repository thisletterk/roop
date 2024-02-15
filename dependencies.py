import subprocess
import sys

def check_dependencies(dependencies):
    missing_dependencies = []
    for dependency in dependencies:
        try:
            __import__(dependency)
        except ImportError:
            missing_dependencies.append(dependency)
    return missing_dependencies

def install_dependencies(dependencies):
    for dependency in dependencies:
        subprocess.call([sys.executable, "-m", "pip", "install", dependency])

def main():
    required_dependencies = ["numpy", "matplotlib", "pandas"]  # Add your required dependencies here
    missing_dependencies = check_dependencies(required_dependencies)

    if missing_dependencies:
        print("The following dependencies are missing and will be installed:")
        print(", ".join(missing_dependencies))
        install_dependencies(missing_dependencies)
        print("Dependencies installed successfully.")
    else:
        print("All dependencies are already installed.")

if __name__ == "__main__":
    main()
