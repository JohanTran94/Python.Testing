# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.

def word_count(text: str) -> int:
    """
    Returnerar antalet ord i en given text.
    """
    return len(text.split())

print(word_count("Python är inte för barn!!!"))