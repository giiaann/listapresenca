@echo off
REM Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install it manually.
    pause
    exit /b 1
)

REM Check if pip is installed
python -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo pip is not installed. Attempting to install it...
    python -m ensurepip --default-pip
    python -m pip install --upgrade pip
    if %errorlevel% neq 0 (
        echo Failed to install pip. Please install it manually.
        pause
        exit /b 1
    )
)

REM Run the Python script to check and install dependencies
python check_and_install_dependencies.py
if %errorlevel% neq 0 (
    echo Failed to check and install dependencies.
    pause
    exit /b 1
)

REM Make the last echoes more visible
echo.
echo ==================================================
echo = All dependencies are installed.                =
echo ==================================================
echo.
echo **Look for another guide inside /distro folder to create a desktop shortcut to the application.**
echo.
echo You can now exit this terminal.
echo.
pause
exit /b 0