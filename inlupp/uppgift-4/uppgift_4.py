# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n: int) -> list[int]:
    """
    Returnerar en lista med de första n Fibonacci-talen.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for x in range(2, n):
        next_fib = fib_sequence[x - 1] + fib_sequence[x - 2]
        fib_sequence.append(next_fib)
    return fib_sequence
print(fibonacci(10))
