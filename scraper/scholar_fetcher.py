from scholarly import scholarly
from NamePrefixRemover import clean_name

def find_best_match(query: dict) -> dict | None:
    """Search author by cleaned name, filter by other criteria, and return filled profile."""
    if not query.get('name'):
        return None

    name = clean_name(query['name'])
    search_res = scholarly.search_author(name)
    for author in search_res:
        profile = scholarly.fill(author)
        
        # filter email domain
        if query.get('email'):
            domain = profile.get('email_domain', '')
            if query['email'].split('@')[-1] not in domain:
                continue

        # filter affiliation
        if query.get('affiliation'):
            aff = profile.get('affiliation', '').lower()
            if query['affiliation'].lower() not in aff:
                continue

        # filter interests/keywords
        if query.get('keywords'):
            interests = [i.lower() for i in profile.get('interests', [])]
            if not any(k.lower() in interests for k in query['keywords']):
                continue

        return profile
    return None
