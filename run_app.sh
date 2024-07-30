#!/bin/bash

# Ensure Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed. Please install it manually."
    exit 1
fi

# Ensure pip is installed
if ! python3 -m pip --version &> /dev/null
then
    echo "pip is not installed. Attempting to install it..."
    python3 -m ensurepip --default-pip
    python3 -m pip install --upgrade pip
fi

# Check and install dependencies
python3 check_and_install_dependencies.py

# Start the Flask app
python3 app.py
