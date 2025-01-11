# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

def count_letters(string: str) -> dict:
    """
    Returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.
    """
    string_count = {}

    for char in string:
        if char.isalpha():
            char = char.lower()
            if char in string_count:
                string_count[char] += 1
            else:
                string_count[char] = 1
    return string_count

print (count_letters("Python är inte för barn"))
