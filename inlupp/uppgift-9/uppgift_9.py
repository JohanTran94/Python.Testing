# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(string: str) -> bool:
    """
    Skriv beskrivning här.
    """
    clean_string = string.replace(" ", "").lower()
    return clean_string == clean_string[::-1]

print(is_palindrome("Radar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))