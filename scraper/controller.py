from abc import ABC, abstractmethod
from .state import query_state
from .scholar_fetcher import find_best_match
from .profile_formatter import format_profile
from time import sleep
import sys

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class EnterCommand(Command):
    def execute(self):
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

class ViewCommand(Command):
    def execute(self):
        print(query_state.view())

class EditCommand(Command):
    def execute(self):
        print(query_state.view())
        print("\nWhich field would you like to edit?")
        print("1. ID")
        print("2. URL")
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

class ClearCommand(Command):
    def execute(self):
        query_state.clear()
        print("✅ All search criteria cleared.")

class SearchCommand(Command):
    def execute(self):
        query = query_state.query
        if not query.get('ID') and not query.get('URL') and not query.get('name'):
            print("⚠️ You must enter a name, URL, or ID before searching.")
            return
        
        print("🔍 Searching Google Scholar", end="")
        sys.stdout.flush()
        for _ in range(3):
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
            filename_base = query.get('name', '') or query.get('ID', '') or query.get('URL', '').split('user=')[-1]
            filename_base = filename_base.replace(' ', '_').replace('/', '_')[:50]
            filename = f"extracted_info_{filename_base}.txt"
            with open(filename, 'w') as f:
                f.write(bio)
            print(f"📝 Profile saved to {filename}.")

class Controller:
    def __init__(self):
        self.commands = {
            '1': EnterCommand(),
            '2': ViewCommand(),
            '3': EditCommand(),
            '4': ClearCommand(),
            '5': SearchCommand()
        }
    
    def execute_command(self, choice):
        command = self.commands.get(choice)
        if command:
            command.execute()
        else:
            print("❌ Invalid choice. Please select 1-6.")