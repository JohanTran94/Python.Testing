# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur från Celsius till Fahrenheit.

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Konverterar en temperatur från Celsius till Fahrenheit.
    """
    return celsius * 9/5 + 32

print (celsius_to_fahrenheit(0))
print (celsius_to_fahrenheit(-40))