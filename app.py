from flask import Flask, request, jsonify, render_template, send_file, redirect, url_for
import csv
import io
import os
import time
import threading
from datetime import datetime

app = Flask(__name__)

# Temporary storage for attendees
attendees = []
backup_folder = 'backups'
os.makedirs(backup_folder, exist_ok=True)

def load_attendees_from_csv(file):
    global attendees
    attendees = []
    file_content = file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(file_content))
    for row in reader:
        attendees.append({
            'name': row['name'],
            'email': row['email'],
            'id': row['id'],
            'checked_in': False,
            'check_in_time': None
        })

def save_attendees_to_csv():
    global attendees
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=['name', 'email', 'id', 'checked_in', 'check_in_time'])
    writer.writeheader()
    writer.writerows([{'name': a['name'], 'email': a['email'], 'id': a['id'], 'checked_in': a['checked_in'], 'check_in_time': a['check_in_time']} for a in attendees])
    return output.getvalue()

def backup_attendees():
    backup_file = os.path.join(backup_folder, f'backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv')
    with open(backup_file, 'w') as f:
        f.write(save_attendees_to_csv())
    print(f"Backup saved to {backup_file}")  # Debug statement
    manage_backups()

def manage_backups():
    backups = sorted(os.listdir(backup_folder), reverse=True)
    if len(backups) > 20:
        for file in backups[20:]:
            os.remove(os.path.join(backup_folder, file))

@app.route('/')
def index():
    return render_template('index.html', loaded_file='No file loaded')

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    try:
        file = request.files['file']
        if not file:
            return jsonify({'error': 'No file uploaded'}), 400

        load_attendees_from_csv(file)
        backup_attendees()
        return jsonify({'message': 'CSV file uploaded successfully', 'attendees': attendees, 'loaded_file': file.filename})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/search_guest', methods=['POST'])
def search_guest():
    try:
        data = request.json
        name = data['name']
        matches = [a for a in attendees if name.lower() in a['name'].lower()]
        return jsonify(matches)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/check_in_guest', methods=['POST'])
def check_in_guest():
    try:
        data = request.json
        name = data['name']
        for attendee in attendees:
            if attendee['name'] == name:
                attendee['checked_in'] = not attendee['checked_in']
                attendee['check_in_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if attendee['checked_in'] else None
                break
        backup_attendees()
        return jsonify(attendees)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/undo_check_in', methods=['POST'])
def undo_check_in():
    try:
        data = request.json
        name = data['name']
        for attendee in attendees:
            if attendee['name'] == name:
                attendee['checked_in'] = not attendee['checked_in']
                attendee['check_in_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if attendee['checked_in'] else None
                break
        backup_attendees()
        return jsonify(attendees)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_attendees', methods=['GET'])
def get_attendees():
    return jsonify(attendees)

@app.route('/get_checked_in_attendees', methods=['GET'])
def get_checked_in_attendees():
    checked_in_attendees = [a for a in attendees if a['checked_in']]
    return jsonify(checked_in_attendees)

@app.route('/generate_report', methods=['GET'])
def generate_report():
    try:
        report_content = save_attendees_to_csv()
        return send_file(
            io.BytesIO(report_content.encode('utf-8')),
            as_attachment=True,
            download_name='report.csv',
            mimetype='text/csv'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reset', methods=['POST'])
def reset():
    global attendees
    attendees = []
    backup_attendees()
    return jsonify({'message': 'Data reset successfully', 'attendees': attendees})

@app.route('/autoload_backup', methods=['GET'])
def autoload_backup():
    backups = sorted(os.listdir(backup_folder), reverse=True)
    if backups:
        latest_backup = backups[0]
        backup_file = os.path.join(backup_folder, latest_backup)
        with open(backup_file, 'r') as f:
            load_attendees_from_csv(io.StringIO(f.read()))
        return jsonify({'message': 'Backup loaded successfully', 'attendees': attendees, 'loaded_file': latest_backup})
    else:
        return jsonify({'message': 'No backups available', 'attendees': []})

if __name__ == '__main__':
    app.run(debug=True)