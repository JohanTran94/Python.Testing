# Uppgift 2
# Skapa en funktion sum_list(numbers) som returnerar summan av alla siffror i listan.

def sum_list(numbers: list[int]) -> int:
    """
    Skriv beskrivning här.
    """
    total = 0
    for number in numbers:
     total = total + number
    return total


print (sum_list([1,2,3,4,5,6]))
