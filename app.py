from flask import Flask, request, jsonify, render_template
import data_manager

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_attendees', methods=['POST'])
def load_attendees():
    file = request.files['file']
    data_manager.load_attendees_from_csv(file)
    return jsonify({'message': 'Attendees loaded successfully'})

@app.route('/add_attendee', methods=['POST'])
def add_attendee():
    name = request.form['name']
    email = request.form['email']
    registration_id = request.form['registration_id']
    data_manager.add_attendee(name, email, registration_id)
    return jsonify({'message': 'Attendee added successfully'})

@app.route('/check_in_attendee', methods=['POST'])
def check_in_attendee():
    registration_id = request.form['registration_id']
    data_manager.check_in_attendee(registration_id)
    return jsonify({'message': 'Attendee checked in successfully'})

@app.route('/undo_check_in', methods=['POST'])
def undo_check_in():
    registration_id = request.form['registration_id']
    data_manager.undo_check_in(registration_id)
    return jsonify({'message': 'Check-in undone successfully'})

@app.route('/generate_report', methods=['GET'])
def generate_report():
    attendees = data_manager.get_checked_in_attendees()
    return jsonify(attendees)

if __name__ == '__main__':
    app.run(debug=True)