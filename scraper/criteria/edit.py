from .. import UsrQueryOptions

def handle(query: dict):
    if not query:
        print("⚠️ No search criteria to edit. Please enter some first.")
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
