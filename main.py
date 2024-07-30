import ui
import data_manager
import check_in

def main():
    data_manager.initialize_database()
    ui.display_main_menu()

if __name__ == "__main__":
    main()