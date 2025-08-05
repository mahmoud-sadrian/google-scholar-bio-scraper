from .. import UsrQueryOptions

def handle(query: dict):
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
