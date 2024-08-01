import data_manager
import check_in

def display_main_menu():
    while True:
        print("\nEvent Attendance Register")
        print("1. Load Attendees from CSV")
        print("2. Add Attendee")
        print("3. Remove Attendee")
        print("4. Check-in Attendee")
        print("5. Undo Check-in")
        print("6. Generate Report")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            load_attendees_from_csv()
        elif choice == '2':
            add_attendee()
        elif choice == '3':
            remove_attendee()
        elif choice == '4':
            check_in_attendee()
        elif choice == '5':
            undo_check_in()
        elif choice == '6':
            generate_report()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def load_attendees_from_csv():
    file_name = input("Enter CSV file name: ")
    data_manager.load_attendees_from_csv(file_name)
    input("Press Enter to go back to the main menu...")

def add_attendee():
    name = input("Enter attendee name: ")
    email = input("Enter attendee email: ")
    registration_id = input("Enter attendee registration ID: ")
    data_manager.add_attendee(name, email, registration_id)
    input("Press Enter to go back to the main menu...")

def remove_attendee():
    registration_id = input("Enter attendee registration ID: ")
    data_manager.remove_attendee(registration_id)
    input("Press Enter to go back to the main menu...")

def check_in_attendee():
    registration_id = input("Enter attendee registration ID: ")
    check_in.check_in_attendee(registration_id)
    input("Press Enter to go back to the main menu...")

def undo_check_in():
    registration_id = input("Enter attendee registration ID: ")
    check_in.undo_check_in(registration_id)
    input("Press Enter to go back to the main menu...")

def generate_report():
    check_in.generate_report()
    input("Press Enter to go back to the main menu...")

def display_attendee_info(attendee):
    if attendee:
        print(f"Name: {attendee[1]}")
        print(f"Email: {attendee[2]}")
        print(f"Registration ID: {attendee[3]}")
        print(f"Checked In: {'Yes' if attendee[4] else 'No'}")
        if attendee[4]:
            print(f"Check-in Time: {attendee[5]}")
    else:
        print("Attendee not found.")