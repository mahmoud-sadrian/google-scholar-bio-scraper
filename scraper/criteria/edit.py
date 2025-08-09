def handle(query_state):
    """Handle editing existing search criteria."""
    print(query_state.view())
    print("\nWhich field would you like to edit?")
    print("1- ID")
    print("2- URL")
    print("3. Name")
    print("4. Email")
    print("5. Affiliation")
    print("6. Interests")
    print("7. Cancel")
    
    choice = input("Enter your choice (1-7): ").strip()
    
    match choice:
        case '1':
            author_id = query_state.input_ID()
            if author_id:
                query_state.update("ID", author_id)
                print("✅ ID updated.")
        case '2':
            author_url = query_state.input_URL()
            if author_url:
                query_state.update("URL", author_url)
                print("✅ URL updated.")
        case '3':
            name = query_state.input_name()
            if name:
                query_state.update("name", name)
                print("✅ Name updated.")
        case '4':
            email = query_state.input_email()
            if email:
                query_state.update("email", email)
                print("✅ Email updated.")
        case '5':
            affiliation = query_state.input_affiliation()
            if affiliation:
                query_state.update("affiliation", affiliation)
                print("✅ Affiliation updated.")
        case '6':
            interests = query_state.input_interests()
            if interests:
                query_state.update("interests", interests)
                print("✅ Interests updated.")
            
        case '7':
            print("No changes made.")
        case _:
            print("❌ Invalid choice.")