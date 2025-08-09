import re
from scraper.NamePrefixRemover import clean_name

class QueryState:
    def __init__(self):
        self.query = {}
    
    def update(self, key, value):
        self.query[key] = value
    
    def get(self, key, default=None):
        return self.query.get(key, default)
    
    def clear(self):
        self.query.clear()
    
    def input_name(self):
        print("Enter the name of the author (e.g., 'Lotfi A. Zadeh'): ")
        name = input().strip()
        return clean_name(name) if name else None

    def input_ID(self):
        print("Enter the author ID (e.g., 'https://scholar.google.com/citations?hl=en&user=\033[1;4mS6H-0RAAAAAJ\033[0m'): ") # Bold and Underline "S6H-0RAAAAAJ"
        author_id = input().strip()
        return author_id if author_id else None

    def input_URL(self):
        print("Enter the author URL (e.g., 'https://scholar.google.com/citations?hl=en&user=S6H-0RAAAAAJ'): ")
        author_url = input().strip()
        return author_url if author_url else None

    def input_email(self):
        print("Enter the email (e.g., 'lotfi@university.edu'): ")
        email = input().strip()
        if email and not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            print("⚠️ Invalid email format.")
            return None
        return email if email else None
    
    def input_affiliation(self):
        print("Enter the affiliation (e.g., 'University of California'): ")
        affiliation = input().strip()
        return affiliation if affiliation else None

    def input_interests(self, case_sensitive=False):
        print("Enter interests (comma-separated, e.g., 'fuzzy logic, artificial intelligence'): ")
        interests = input().strip()
        if not case_sensitive:
            return [i.strip().lower() for i in interests.split(',')] if interests else []
        return [i.strip() for i in interests.split(',')] if interests else []

    def view(self):
        if not self.query:
            return "No search criteria entered."
        lines = ["Current search criteria:"]
        for key, value in self.query.items():
            if key == "keywords" and isinstance(value, list):
                value = ", ".join(value) if value else "None"
            lines.append(f"{key.capitalize()}: {value or 'None'}")
        return "\n".join(lines)

query_state = QueryState()