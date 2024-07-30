import subprocess
import sys

def check_python_version():
    try:
        subprocess.check_output(['python3', '--version'])
    except FileNotFoundError:
        print("Python 3 is not installed. Please install it manually.")
        sys.exit(1)

def check_pip_installed():
    try:
        subprocess.check_output(['python3', '-m', 'pip', '--version'])
    except subprocess.CalledProcessError:
        print("pip is not installed. Attempting to install it...")
        try:
            subprocess.check_call(['python3', '-m', 'ensurepip', '--default-pip'])
            subprocess.check_call(['python3', '-m', 'pip', 'install', '--upgrade', 'pip'])
        except subprocess.CalledProcessError:
            print("Failed to install pip. Please install it manually.")
            sys.exit(1)

def check_and_install_dependencies():
    check_python_version()
    check_pip_installed()

    with open('requirements.txt') as f:
        dependencies = f.read().splitlines()

    for dependency in dependencies:
        try:
            __import__(dependency.split('==')[0])
            print(f'{dependency} is already installed.')
        except ImportError:
            print(f'{dependency} is not installed. Installing...')
            subprocess.check_call(['python3', '-m', 'pip', 'install', dependency])
            print(f'{dependency} has been installed.')

if __name__ == '__main__':
    check_and_install_dependencies()