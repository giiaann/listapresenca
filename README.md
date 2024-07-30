# Event Attendance Management System

## Overview

The Event Attendance Management System is a very basic web application designed to manage events in its early stages.

## Structure

- **`app.py`**: The main Flask application file that handles routing and business logic.
- **`templates/index.html`**: The main HTML file for the frontend interface.
- **`static/styles.css`**: CSS file for styling the frontend.
- **`static/scripts.js`**: JavaScript file for handling frontend interactions.
- **`requirements.txt`**: Lists all Python dependencies.
- **`run_app.sh`**: Shell script to run the application on Linux.
- **`run_app.bat`**: Batch file to run the application on Windows.
- **`check_and_install_dependencies.py`**: Python script to check and install dependencies.

# Event Attendance Management System Introduction

Welcome to the Event Attendance Management System! This application helps you manage event attendance by uploading a CSV file of attendees, checking them in, and generating simple reports. Below, you'll find a step-by-step guide to help you get started.

## Prerequisites

- A computer running Linux (e.g., Ubuntu, Fedora)
- Basic knowledge of using a file manager and a terminal

## Installing Python and pip

Before you can run the application, you need to ensure that Python 3 and pip are installed on your system.

### Installing Python 3

1. **Open a Terminal**:
   - Right-click on your desktop or in a folder and select "Open in Terminal" (the exact wording may vary depending on your file manager).

2. **Update Package List**:
   - Run the following command to update your package list:
     ```sh
     sudo apt update
     ```

3. **Install Python 3**:
   - Run the following command to install Python 3:
     ```sh
     sudo apt install python3
     ```

### Installing pip

1. **Install pip**:
   - Run the following command to install pip, the package installer for Python:
     ```sh
     sudo apt install python3-pip
     ```

## Installation

1. **Download the Application**:
   - Download the application files from the repository or receive them from a colleague. The files should include the `Event_AttendanceApp` script, the `dist` folder containing the executable `app`, and the `check_and_install_dependencies.py` script.

2. **Navigate to the Application Folder**:
   - Open your file manager (e.g., Nautilus, Dolphin) and navigate to the folder where you downloaded the application files.

3. **Open a Terminal**:
   - Right-click within the application folder and select "Open in Terminal" (the exact wording may vary depending on your file manager).

4. **Check and Install Dependencies**:
   - In the terminal, type the following command and press `Enter`:
     
     python3 check_and_install_dependencies.py
    
   - This script will ensure that all required packages are installed.

## Running the Application

1. **Run the Application**:
   - In the terminal, type the following command and press `Enter`:
     
     ./Event_AttendanceApp
     
   - This will start the application, and you should see output indicating that the Flask server is running.

2. **Access the Web Interface**:
   - Open a web browser (e.g., Firefox, Chrome) and navigate to `http://127.0.0.1:5000`.
   - You should see the Event Attendance Management System web interface.

## Using the Application

1. **Upload a CSV File**:
   - On the web interface, locate the "Upload CSV" section.
   - Click the "Choose File" button and select the CSV file containing your attendees' information.
   - Click the "Upload" button to upload the file.

2. **Search for an Attendee**:
   - In the "Search Guest" section, enter the name of the attendee you want to search for.
   - Click the "Search" button.
   - The application will display any matching attendees.

3. **Check In/Out an Attendee**:
   - In the "Guest Details" section, you will see a checkbox next to each attendee's name.
   - Click the checkbox to check in or check out the attendee.
   - A confirmation dialog will appear to confirm the action.

4. **Generate a Report**:
   - In the top menu, select "Generate Report".
   - The application will generate a CSV file containing the current attendance status of all attendees.
   - The file will be downloaded to your computer.

## Troubleshooting

- **Application Doesn't Start**:
  - Ensure you are in the correct folder and have executed the `Event_AttendanceApp` script.
  - Check the terminal output for any error messages and try to resolve them.

- **Web Interface Not Loading**:
  - Ensure your web browser is pointing to `http://127.0.0.1:5000`.
  - Check if the Flask server is running by looking at the terminal output.

## Support

If you encounter any issues or need further assistance, please contact our support team at [giancarlo.guimaraes21@gmail.com](mailto:support@example.com).

Thank you for using the Event Attendance Management System! We hope it helps you manage your events efficiently.


## Future updates

Full PT-BR language translation 
Language selection
Windows port with documentation and executable (.exe)
Add/remove atteattendance on demand
Customize backupfolder