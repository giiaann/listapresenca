from flask import Flask, request, jsonify, render_template, send_file
import csv
import io

app = Flask(__name__)

# Temporary storage for attendees
attendees = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    try:
        file = request.files['file']
        if not file:
            return jsonify({'error': 'No file uploaded'}), 400

        # Read the CSV file
        global attendees
        attendees = []
        reader = csv.DictReader(file.read().decode('utf-8').splitlines())
        for row in reader:
            attendees.append({
                'name': row['name'],
                'email': row['email'],
                'registration_id': row['id'],
                'checked_in': False
            })

        return jsonify(attendees)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/add_attendee', methods=['POST'])
def add_attendee():
    try:
        data = request.json
        attendees.append({
            'name': data['name'],
            'email': data['email'],
            'registration_id': data['registration_id'],
            'checked_in': False
        })
        return jsonify({'message': 'Attendee added successfully', 'attendees': attendees})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/remove_attendee', methods=['POST'])
def remove_attendee():
    try:
        data = request.json
        attendees[:] = [a for a in attendees if a['registration_id'] != data['registration_id']]
        return jsonify({'message': 'Attendee removed successfully', 'attendees': attendees})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/check_in_attendee', methods=['POST'])
def check_in_attendee():
    try:
        data = request.json
        for attendee in attendees:
            if attendee['registration_id'] == data['registration_id']:
                attendee['checked_in'] = True
                break
        return jsonify({'message': 'Attendee checked in successfully', 'attendees': attendees})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/undo_check_in', methods=['POST'])
def undo_check_in():
    try:
        data = request.json
        for attendee in attendees:
            if attendee['registration_id'] == data['registration_id']:
                attendee['checked_in'] = False
                break
        return jsonify({'message': 'Check-in undone successfully', 'attendees': attendees})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_attendees', methods=['GET'])
def get_attendees():
    return jsonify(attendees)

@app.route('/reset', methods=['POST'])
def reset():
    global attendees
    attendees = []
    return jsonify({'message': 'Data reset successfully', 'attendees': attendees})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    checked_in_count = sum(1 for attendee in attendees if attendee['checked_in'])
    missing_count = len(attendees) - checked_in_count

    report = f"Event Report\n\n"
    report += f"Total Attendees: {len(attendees)}\n"
    report += f"Checked-in Attendees: {checked_in_count}\n"
    report += f"Missing Attendees: {missing_count}\n"

    buffer = io.BytesIO()
    buffer.write(report.encode('utf-8'))
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name='report.txt', mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)