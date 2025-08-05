import re

# List of known prefixes to remove
prefixes_to_remove = [
    "dr", "prof", "professor", "doctor", "lect", "lecturer", "master",
    "mr", "mrs", "ms", "miss", "mx",
    "capt", "captain", "col", "colonel", "maj", "major",
    "lt", "lieutenant", "gen", "general", "sgt", "sergeant",
    "sir", "dame", "hon", "honorable", "rt. hon",
    "rev", "reverend", "fr", "father", "rabbi", "imam", "sheikh", "pastor"
]


clean_name_pattern = r'^(' + '|'.join(re.escape(p) + r'\.?' for p in prefixes_to_remove) + r')\s+'

def clean_name(name: str) -> str:
    """Recursively removes known prefixes from the start of a name."""
    old = None
    while old != name:
        old = name
        name = re.sub(clean_name_pattern, '', name, flags=re.IGNORECASE).strip()
    return name

# test_names = [
#     "Dr. Jane Doe",
#     "Prof. Dr. Max Müller",
#     "Mr Ali Reza",
#     "Lt. Col. Amir Hosseini",
#     "Professor John Smith",
#     "Father Joseph",
#     "Reverend Dr. Sarah Connor",
#     "Sir Isaac Newton",
#     "Rt. Hon. Prof. Albert Einstein"
# ]

# for name in test_names:
#     cleaned = clean_name(name)
#     print(f"{name}  →  {cleaned}")
