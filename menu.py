import time
import os
from scraper import UsrQueryOptions

# Global query state
query = {}

def clear_console():
    """Clear the console screen on any OS."""
    os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    """Display the main menu and handle user choices."""
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
                enter_search_criteria()
            case '2':
                view_search_criteria()
            case '3':
                edit_search_criteria()
            case '4':
                clear_search_criteria()
            case '5':
                exit_program()
            case _:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)
                clear_console()

def enter_search_criteria():
    """Prompt user for search criteria input."""
    print("✏️ Enter search criteria (press Enter to skip a field):\n")
    name = UsrQueryOptions.user_input_name()
    email = UsrQueryOptions.user_input_email()
    affiliation = UsrQueryOptions.user_input_affiliation()
    keywords = UsrQueryOptions.user_input_keywords()

    if name: query['name'] = name
    if email: query['email'] = email
    if affiliation: query['affiliation'] = affiliation
    if keywords: query['keywords'] = keywords

    print("\n✅ Search criteria updated.")
    input("\nPress Enter to return to the menu...")
    clear_console()

def view_search_criteria():
    """Display the current search criteria."""
    if not query:
        print("ℹ️  No search criteria set.")
    else:
        print("📄 Current search criteria:\n")
        for key, value in query.items():
            print(f"• {key.capitalize()}: {value}")

    input("\nPress Enter to return to the menu...")
    clear_console()

def edit_search_criteria():
    """Allow user to edit search criteria."""
    if not query:
        print("⚠️ No search criteria to edit. Please enter some first.")
        input("\nPress Enter to return to the menu...")
        clear_console()
        return

    print("✏️ Edit search criteria (leave blank to keep current value):\n")
    for key, value in query.items():
        print(f"Current {key.capitalize()}: {value}")
    print("\n" + "-" * 60)

    name = UsrQueryOptions.user_input_name()
    email = UsrQueryOptions.user_input_email()
    affiliation = UsrQueryOptions.user_input_affiliation()
    keywords = UsrQueryOptions.user_input_keywords()

    if name: query['name'] = name
    if email: query['email'] = email
    if affiliation: query['affiliation'] = affiliation
    if keywords: query['keywords'] = keywords

    print("\n✅ Search criteria updated.")
    input("\nPress Enter to return to the menu...")
    clear_console()

def clear_search_criteria():
    """Clear all user search criteria."""
    query.clear()
    print("🗑️ Search criteria cleared.")
    input("\nPress Enter to return to the menu...")
    clear_console()

def exit_program():
    """Exit the program gracefully."""
    print("👋 Exiting the program. Goodbye!")
    time.sleep(0.5)
    clear_console()
    exit()

if __name__ == "__main__":
    main_menu()
