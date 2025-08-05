import time
import os
from scraper.state import query
from scraper.criteria import enter, view, edit, clear

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def wait_return():
    input("\nPress Enter to return to the menu...")
    clear_console()

def main_menu():
    while True:
        print("📚 Welcome to the Google Scholar Bio Scraper!")
        print("--------------------------------------------")
        print("Please choose an option:")
        print("1. Enter search criteria")
        print("2. View current search criteria")
        print("3. Edit search criteria")
        print("4. Clear search criteria")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        clear_console()

        match choice:
            case '1':
                enter.handle(query)
                wait_return()
            case '2':
                view.handle(query)
                wait_return()
            case '3':
                edit.handle(query)
                wait_return()
            case '4':
                clear.handle(query)
                wait_return()
            case '5':
                print("👋 Exiting the program. Goodbye!")
                time.sleep(0.5)
                clear_console()
                exit()
            case _:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)
                clear_console()
