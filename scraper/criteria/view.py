def handle(query: dict):
    if not query:
        print("ℹ️  No search criteria set.")
        return

    print("📄 Current search criteria:\n")
    for key, value in query.items():
        print(f"• {key.capitalize()}: {value}")
