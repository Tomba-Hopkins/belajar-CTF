# hasil dari gpt noh

def format_name(name):
    parts = name.strip().split()
    if len(parts) != 2:
        return []

    first, last = parts
    combos = [
        f"{first}.{last}",
        f"{first[0]}.{last}",
        f"{last}.{first}",
        f"{last}.{first[0]}",
        f"{first}{last}",
        f"{first[0]}{last}",
        f"{first}",
        f"{last}",
        f"{first.capitalize()}.{last.capitalize()}",
        f"{first[0].upper()}-{last.capitalize()}",
        f"{last.capitalize()}.{first[0].upper()}",
    ]

    return list(set(combos))  # remove duplicates

with open("names.txt") as f:
    names = [line.strip() for line in f if line.strip()]

for name in names:
    for u in format_name(name):
        print(u)

