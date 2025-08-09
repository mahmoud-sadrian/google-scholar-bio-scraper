def handle(query_state):
    print("Enter new search criteria (leave blank to skip) ↓\n")

    name = query_state.input_name()
    if name:
        query_state.update("name", name)
    
    email = query_state.input_email()
    if email:
        query_state.update("email", email)
    
    affiliation = query_state.input_affiliation()
    if affiliation:
        query_state.update("affiliation", affiliation)

    interests = query_state.input_interests()
    if interests:
        query_state.update("interests", interests)

    print("\n✅ Search criteria updated.")