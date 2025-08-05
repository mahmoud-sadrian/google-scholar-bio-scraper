def format_profile(profile: dict, max_pubs: int = 5) -> str:
    """Format profile dict into a readable bio."""
    lines = []
    # Basic info
    lines.append(f"Name: {profile.get('name', 'N/A')}")
    lines.append(f"Affiliation: {profile.get('affiliation', 'N/A')}")
    email_dom = profile.get('email_domain', '')
    lines.append(f"Email: Verified at {email_dom.lstrip('@')}" if email_dom else "Email: N/A")

    scholar_id = profile.get('scholar_id')
    if scholar_id:
        link = f"https://scholar.google.com/citations?user={scholar_id}"
        lines.append(f"Google Scholar: {link}")
    else:
        lines.append("Google Scholar: N/A")

    # Citation metrics
    all_cites = profile.get('citedby', 0)
    all_h = profile.get('hindex', 0)
    all_i10 = profile.get('i10index', 0)
    # Since year filtering requires additional data: skip due to scholarly limitations
    lines.append(f"\nCitations: {all_cites:,} (All time)")
    lines.append(f"h-index: {all_h} (All time)")
    lines.append(f"i10-index: {all_i10} (All time)")

    # Interests
    interests = profile.get('interests', [])
    if interests:
        lines.append("\nResearch Interests: " + ", ".join(interests))

    # Publications
    pubs = profile.get('publications', [])[:max_pubs]
    if pubs:
        lines.append("\nTop Publications:")
        for i, pub in enumerate(pubs, 1):
            bib = pub.get('bib', {})
            title = bib.get('title', 'Untitled')
            authors = bib.get('author', '')
            venue = bib.get('venue', '')
            year = bib.get('pub_year', '?')
            cites = pub.get('num_citations', 0)
            lines.append(f'{i}. "{title}", {authors} – {venue} {year}. Citations: {cites}')

    # Co-authors
    coauthors = profile.get('co_authors', [])
    if coauthors:
        lines.append("\nTop Co-authors:")
        for co in coauthors[:3]:
            lines.append(f"- {co.get('name')} (https://scholar.google.com/citations?user={co.get('scholar_id')})")

    return "\n".join(lines)
