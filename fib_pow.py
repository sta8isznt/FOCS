import math

def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    return round(pow(phi, n) / math.sqrt(5))

# Example usage:
n = 1000
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")