import numpy as np

def matrix_mult(A, B):
    return np.dot(A, B)

def matrix_power(matrix, n):
    result = np.identity(len(matrix), dtype=int)
    base = matrix

    while n > 0:
        if n % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        n //= 2

    return result

def fibonacci_matrix(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    F = np.array([[1, 1], [1, 0]], dtype=int)
    result = matrix_power(F, n-1)
    return result[0][0]

n = 10
print(f"Fibonacci number at position {n} is {fibonacci_matrix(n)}")