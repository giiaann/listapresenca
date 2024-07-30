import csv
import sqlite3

DATABASE_NAME = 'event_attendance.db'

def initialize_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attendees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            registration_id TEXT NOT NULL,
            checked_in BOOLEAN DEFAULT 0,
            check_in_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

def load_attendees_from_csv(file_name):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
                INSERT INTO attendees (name, email, registration_id)
                VALUES (?, ?, ?)
            ''', (row['name'], row['email'], row['registration_id']))
    conn.commit()
    conn.close()

def add_attendee(name, email, registration_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO attendees (name, email, registration_id)
        VALUES (?, ?, ?)
    ''', (name, email, registration_id))
    conn.commit()
    conn.close()

def remove_attendee(registration_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM attendees WHERE registration_id = ?
    ''', (registration_id,))
    conn.commit()
    conn.close()

def get_attendee(registration_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM attendees WHERE registration_id = ?
    ''', (registration_id,))
    attendee = cursor.fetchone()
    conn.close()
    return attendee

def mark_attendee_checked_in(registration_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE attendees SET checked_in = 1, check_in_time = datetime('now')
        WHERE registration_id = ?
    ''', (registration_id,))
    conn.commit()
    conn.close()

def undo_check_in(registration_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE attendees SET checked_in = 0, check_in_time = NULL
        WHERE registration_id = ?
    ''', (registration_id,))
    conn.commit()
    conn.close()

def get_checked_in_attendees():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM attendees WHERE checked_in = 1
    ''')
    attendees = cursor.fetchall()
    conn.close()
    return attendees