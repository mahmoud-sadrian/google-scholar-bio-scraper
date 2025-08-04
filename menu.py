import time
import UsrQueryOptions

query = {}

def enter_page():
    print("Welcome to the Google Scholar Bio Scraper!")
    print("Please choose an option:")
    print("1. Enter search criteria")
    print("2. View current search criteria")
    print("3. Edit search criteria")
    print("4. Clear search criteria")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()
    # clear console
    print("\033c", end="")
    
    if choice == '1':
        enter_search_criteria()
    elif choice == '2':
        view_search_criteria()
    elif choice == '3':
        edit_search_criteria()
    elif choice == '4':
        clear_search_criteria()
    elif choice == '5':
        exit_program()
    else:
        print("Invalid choice. Please try again.")

        # wait and clear console
        
        time.sleep(2)
        print("\033c", end="") 
  
        enter_page()

def enter_search_criteria():
    print("If you want to skip a criteria, just press Enter\n")
    name = UsrQueryOptions.user_input_name()
    email = UsrQueryOptions.user_input_email()
    affiliation = UsrQueryOptions.user_input_affiliation()
    keywords = UsrQueryOptions.user_input_keywords()
    
    if name:
        query['name'] = name
    if email:
        query['email'] = email
    if affiliation:
        query['affiliation'] = affiliation
    if keywords:
        query['keywords'] = keywords
    
    print()
    print("Search criteria updated.")

    print()
    input("Press Enter to return to the main menu...")
    # clear console
    print("\033c", end="")

    enter_page()

def view_search_criteria():
    if not query:
        print("No search criteria set.")
    else:
        print("Current search criteria:")
        for key, value in query.items():
            print(f"{key.capitalize()}: {value}")

    print()
    input("Press Enter to return to the main menu...")
    # clear console
    print("\033c", end="")

    enter_page()

def edit_search_criteria():
    if not query:
        print("No search criteria set. Please enter search criteria first.")
        print()
        input("Press Enter to return to the main menu...")
        # clear console
        print("\033c", end="")
        enter_page()
        return

    print("Current search criteria:")
    for key, value in query.items():
        print(f"{key.capitalize()}: {value}")

    print("\nEnter new values for the criteria you want to change (leave blank to keep current value):\n")
    
    name = UsrQueryOptions.user_input_name()
    email = UsrQueryOptions.user_input_email()
    affiliation = UsrQueryOptions.user_input_affiliation()
    keywords = UsrQueryOptions.user_input_keywords()

    if name:
        query['name'] = name
    if email:
        query['email'] = email
    if affiliation:
        query['affiliation'] = affiliation
    if keywords:
        query['keywords'] = keywords
    
    print()
    print("Search criteria updated.")

    print()
    input("Press Enter to return to the main menu...")
    # clear console
    print("\033c", end="")

    enter_page()

def clear_search_criteria():
    query.clear()
    print("Search criteria cleared.")

    print()
    input("Press Enter to return to the main menu...")
    # clear console
    print("\033c", end="")

    enter_page()

def exit_program():
    print("Exiting the program. Goodbye!")
    time.sleep(1)
    exit()

if __name__ == "__main__":
    enter_page()


