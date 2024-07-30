# Event Attendance Management System

Welcome to the Event Attendance Management System! This application helps you manage event attendance by uploading a CSV file of attendees, checking them in, and generating reports. Below, you'll find a step-by-step guide to help you get started, even if you're new to Linux.

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

<<<<<<< HEAD
2. **Navigate to the Application Folder**:
   - Open your file manager (e.g., Nautilus, Dolphin) and navigate to the folder where you downloaded the application files.
=======
1. **Clone the repository:**
   ```bash
   git clone https://github.com/giiaann/listapresenca.git
   cd event-attendance-management
   run the script (./run_app.sh) located inside listapresenca folder.
>>>>>>> 55af5f38f625ab7d756f5e2f022ed8e935dfd244

3. **Open a Terminal**:
   - Right-click within the application folder and select "Open in Terminal" (the exact wording may vary depending on your file manager).

<<<<<<< HEAD
4. **Check and Install Dependencies**:
   - In the terminal, type the following command and press `Enter`:
     ```sh
     python3 check_and_install_dependencies.py
     ```
   - This script will ensure that all required packages are installed.

## Running the Application

1. **Run the Application**:
   - In the terminal, type the following command and press `Enter`:
     ```sh
     ./Event_AttendanceApp
     ```
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
=======
1. **Clone the repository:**
   
    https://github.com/giiaann/listapresenca.git
 
    run "run_app.bat" to ensure Python and pip are installed and runs the application.
    The executable will be located in the dist directory - dist\app.exe
>>>>>>> 55af5f38f625ab7d756f5e2f022ed8e935dfd244
