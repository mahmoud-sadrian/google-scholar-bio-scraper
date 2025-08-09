from scholarly import scholarly
from .NamePrefixRemover import clean_name
import re
from time import sleep

def find_best_match(query: dict) -> dict | None:
    """Search author by ID, URL, or cleaned name, filter by other criteria, and return filled profile."""
    retries = 3
    for attempt in range(retries):
        try:
            # Extract scholar ID from URL if provided
            scholar_id = query.get('ID')
            if not scholar_id and query.get('URL'):
                url = query['URL']
                match = re.search(r'user=([a-zA-Z0-9_-]+)', url)
                if match:
                    scholar_id = match.group(1)

            # Search by scholar ID if available
            if scholar_id:
                author = scholarly.search_author_id(scholar_id)
                profile = scholarly.fill(author)
                return profile

            # Fallback to name-based search if no ID/URL
            if not query.get('name'):
                return None

            name = clean_name(query['name'])
            search_res = scholarly.search_author(name)
            for author in search_res:
                profile = scholarly.fill(author)
                
                # Filter email domain
                if query.get('email'):
                    domain = profile.get('email_domain', '')
                    if query['email'].split('@')[-1] not in domain:
                        continue

                # Filter affiliation
                if query.get('affiliation'):
                    aff = profile.get('affiliation', '').lower()
                    if query['affiliation'].lower() not in aff:
                        continue

                # Filter interests
                if query.get('interests'):
                    interests = [i.lower() for i in profile.get('interests', [])]
                    if not any(k.lower() in interests for k in query['interests']):
                        continue

                return profile
            return None
        except Exception as e:
            if attempt < retries - 1:
                sleep(2 ** attempt)  # Exponential backoff
                continue
            print(f"⚠️ Failed after {retries} attempts: {e}")
            return None
    return None