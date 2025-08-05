import time
import os
from scraper.state import query
from scraper.criteria import enter, view, edit, clear, search

def clear_console(sleep_time=0.0):
    time.sleep(sleep_time)
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
        print("5. Search and show Google Scholar profile")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
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
                search.handle(query)
                wait_return()
            case '6':
                print("👋 Exiting the program. Goodbye!")
                clear_console(0.5)
                exit()
            case _:
                print("❌ Invalid choice. Please try again.")
                clear_console(1)
