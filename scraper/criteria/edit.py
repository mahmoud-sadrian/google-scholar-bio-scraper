def handle(query_state):
    """Handle editing existing search criteria."""
    print(query_state.view())
    print("\nWhich field would you like to edit?")
    print("1. Name")
    print("2. Email")
    print("3. Affiliation")
    print("4. Keywords")
    print("5. Cancel")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    match choice:
        case '1':
            name = query_state.input_name()
            if name:
                query_state.update("name", name)
                print("✅ Name updated.")
        case '2':
            email = query_state.input_email()
            if email:
                query_state.update("email", email)
                print("✅ Email updated.")
        case '3':
            affiliation = query_state.input_affiliation()
            if affiliation:
                query_state.update("affiliation", affiliation)
                print("✅ Affiliation updated.")
        case '4':
            keywords = query_state.input_keywords()
            if keywords:
                query_state.update("keywords", keywords)
                print("✅ Keywords updated.")
        case '5':
            print("No changes made.")
        case _:
            print("❌ Invalid choice.")