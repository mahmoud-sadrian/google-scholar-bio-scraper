def user_input_name():
    print("Enter the name of the author you want to search for: (Example: 'Lotfi A. Zadeh')")
    search_query = input().strip()
    if not search_query:
        print("Search query cannot be empty. Please try again.")
        return user_input_name()
    return search_query if search_query else None

def user_input_email():
    print("Enter the email (e.g., 'lotfi@university.edu')")
    email = input().strip()
    return email if email else None

def user_input_affiliation():
    print("Enter the affiliation (e.g., 'University of California')")
    affiliation = input().strip()
    return affiliation if affiliation else None

def user_input_keywords():
    print("Enter keywords (comma-separated, e.g., 'fuzzy logic, artificial intelligence')")
    keywords = input().strip()
    return [kw.strip() for kw in keywords.split(',')] if keywords else []