# Event Attendance Management System V1.0.2

Welcome to the Event Attendance Management System! This application helps you manage event attendance by uploading a CSV file of attendees, checking them in, and generating reports. Below, you'll find a step-by-step guide to help you get started.

## Prerequisites

- A computer running Windows 10/11;
- Basic knowledge of using a file manager and a terminal.

## Installing Python and pip

Before you can run the application, you need to ensure that Python 3 and pip are installed on your system. 
 *IMPORTANT* - Set it as environment variable during install.
 Check for the latest version at https://www.python.org/downloads/

## Installation

1. **Download the Application**:
   - Download the application files from the repository (from https://github.com/giiaann/listapresenca.git) or receive them from a colleague. The files should include the main files alongside some scripts to be covered later in this guide.

2. **Navigate to the Application Folder**:
   - Open your file manager and navigate to the folder where you downloaded and unzip the application files. The application has been tested running from /documents and /desktop, so any of those will work fine.

=======

1. **Check and Install Dependencies**:

For Windows users, the application is meant to ready for use. But, to make sure you have all libs and dependencies, there is one check_install.bat script that should check everything for you.

## Running the Application

1. **Create shortcut/ run the .exe**:
   - Inside the "listapresenca-main" folder there are the main files and a folder called "dist".
   - Inside "dist" folder should be a app.exe file, which is the one you should create the shortcut for. There is a .txt file inside this folder that will help you if you don't know how to create a shortcut.
   - After running the app, you should see the Event Attendance Management System web console.
 
   *** VERY IMPORTANT: It is essential you keep this terminal open while you want the application running ***
   
2. **Access the Web Interface**:
   - Open a web browser (e.g., Firefox, Chrome) and navigate to `http://127.0.0.1:5000`.
   - You should see the Event Attendance Management System web interface.

## Using the Application

1. **Upload a CSV File**:
   - On the web interface, locate the "Upload CSV" section.
   - Click the "Choose File" button and select the CSV file containing your attendees' information.
   - Click the "Upload" button to upload the file.
   - Inside "dist" folder, another folder called "backups" will save up to 15 "backups" of your work.
      - They will be saved in a format like this: "archive_yyyymmdd_hh:mm:ss" in order to the user recognize which one is the latest one.
   - There is one testlist.csv inside "testlist" folder so you can play with before inserting your .csv file.

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
