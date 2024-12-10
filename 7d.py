import time
import numpy as np
import sys

sys.set_int_max_str_digits(10000)

def fib(n):
    def fib_pair(n):
        if n == 0:
            return (0, 1)
        else:
            a, b = fib_pair(n // 2) #a = F(n//2), b = F(n//2 +1)
            c = a * ((b << 1) - a)
            d = a * a + b * b
            if n % 2 == 1:
                return (d, c + d) # Returns F(2k+1), F(2k+2) = F(2k) + F(2k+1)
            else:
                return (c, d)

    return fib_pair(n)[0]

def matrix_mult(A, B):
    return np.dot(A, B)

def matrix_power(matrix, n):
    result = np.identity(len(matrix), dtype=object)
    base = matrix.astype(object)

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

    F = np.array([[1, 1], [1, 0]], dtype=object)
    result = matrix_power(F, n-1)
    return result[0][0]

def compare_methods(n):
    start_time = time.time()
    fib(n)
    time_fib = time.time() - start_time

    start_time = time.time()
    fibonacci_matrix(n)
    time_matrix = time.time() - start_time

    print(f"Fibonacci pair method: {time_fib:.6f} seconds")
    print(f"Fibonacci matrix method: {time_matrix:.6f} seconds")

n = 10
print(f"The {n}th Fibonacci number is: {fib(n)}")

n = 10 ** 5
compare_methods(n)