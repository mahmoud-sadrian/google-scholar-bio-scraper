from ..scholar_fetcher import find_best_match
from ..profile_formatter import format_profile
from time import sleep
import sys

def handle(query: dict):
    if ('ID' not in query or not query['ID'].strip()) and ('URL' not in query or not query['URL'].strip()):
        print("⚠️ You must enter an URL/ID before searching.")
        return

    print("🔍 Searching Google Scholar", end="")
    sys.stdout.flush()
    for i in range(3):
        print(".", end="", flush=True)
        sleep(0.5)
    print("\n")
    
    profile = find_best_match(query)
    if not profile:
        print("❌ No matching profile found.")
        return

    bio = format_profile(profile)
    print("✅ Profile Found:\n")
    print(bio)
    
    save = input("\nSave to file? (y/n): ").strip().lower()
    if save == 'y':
        filename = f"extracted_info_{query['name'].replace(' ', '_')}.txt"
        with open(filename, 'w') as f:
            f.write(bio)
        print(f"📝 Profile saved to {filename}.")