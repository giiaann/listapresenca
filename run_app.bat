@echo off

:: Ensure Python 3 is installed
where python >nul 2>nul
if %errorLevel% neq 0 (
    echo Python is not installed. Please install it manually.
    exit /b 1
)

:: Ensure pip is installed
python -m pip --version >nul 2>nul
if %errorLevel% neq 0 (
    echo pip is not installed. Attempting to install it...
    python -m ensurepip --default-pip
    python -m pip install --upgrade pip
)

:: Check and install dependencies
python check_and_install_dependencies.py

:: Start the Flask app
python app.py