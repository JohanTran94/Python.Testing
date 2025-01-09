# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.

def validate_password(password: str) -> bool:
    """
    Skriv beskrivning här.
    """
    if len(password) >= 8 and any(char.isdigit() for char in password):
        return True
    return False

print (validate_password("abc123abr"))
print (validate_password("ancjj"))
print (validate_password("anhknfhty"))
print (validate_password("123654789"))
