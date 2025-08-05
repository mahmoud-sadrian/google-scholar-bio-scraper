from ..scholar_fetcher import find_best_match
from ..profile_formatter import format_profile

def handle(query: dict):
    if 'name' not in query or not query['name'].strip():
        print("⚠️ You must enter a name before searching.")
        return

    print("🔍 Searching Google Scholar...\n")
    profile = find_best_match(query)

    if not profile:
        print("❌ No matching profile found.")
        return

    bio = format_profile(profile)
    print("✅ Profile Found:\n")
    print(bio)
