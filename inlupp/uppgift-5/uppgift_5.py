# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.

def filter_odd(numbers: int) -> list[int]:
    """
    Returnerar en lista med alla jämna tal från den givna listan.
    """
    jämna_nummer = [num for num in numbers if num % 2 == 0]
    return jämna_nummer

print (filter_odd([1,2,3,4,5,6,7,8,9,10]))