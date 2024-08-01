import data_manager
import ui

def check_in_attendee(registration_id):
    attendee = data_manager.get_attendee(registration_id)
    if attendee:
        if attendee[4]:
            print("Attendee is already checked in.")
        else:
            data_manager.mark_attendee_checked_in(registration_id)
            print("Attendee checked in successfully.")
    else:
        print("Attendee not found.")

def undo_check_in(registration_id):
    attendee = data_manager.get_attendee(registration_id)
    if attendee:
        if not attendee[4]:
            print("Attendee is not checked in.")
        else:
            data_manager.undo_check_in(registration_id)
            print("Check-in undone successfully.")
    else:
        print("Attendee not found.")

def generate_report():
    attendees = data_manager.get_checked_in_attendees()
    if attendees:
        print("Checked-in Attendees:")
        for attendee in attendees:
            ui.display_attendee_info(attendee)
    else:
        print("No attendees have checked in yet.")