import subprocess
import sys
import platform

def check_python_version():
    try:
        subprocess.check_output([sys.executable, '--version'])
    except FileNotFoundError:
        print("Python is not installed. Please install it manually.")
        sys.exit(1)

def check_pip_installed():
    try:
        subprocess.check_output([sys.executable, '-m', 'pip', '--version'])
    except subprocess.CalledProcessError:
        print("pip is not installed. Attempting to install it...")
        try:
            subprocess.check_call([sys.executable, '-m', 'ensurepip', '--default-pip'])
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install pip: {e}. Please install it manually.")
            sys.exit(1)

def check_and_install_dependencies():
    check_python_version()
    check_pip_installed()

    with open('requirements.txt') as f:
        dependencies = f.read().splitlines()

    for dependency in dependencies:
        if dependency.startswith('#'):
            continue
        if '==' in dependency:
            package_name, version = dependency.split('==')
            if platform.system() == 'Windows' and package_name == 'command-not-found':
                print(f'Skipping {dependency} on Windows.')
                continue

        try:
            subprocess.check_output([sys.executable, '-m', 'pip', 'show', package_name])
            print(f'{dependency} is already installed.')
        except subprocess.CalledProcessError:
            print(f'{dependency} is not installed. Installing...')
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])
                print(f'{dependency} has been installed.')
            except subprocess.CalledProcessError as e:
                print(f"Failed to install {dependency}: {e}. Please install it manually.")
                sys.exit(1)

if __name__ == '__main__':
    check_and_install_dependencies()