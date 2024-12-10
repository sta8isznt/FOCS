import time
import numpy as np

def matrix_mult(A, B):
    return np.dot(A, B).astype(object)

def matrix_power(matrix, n):
    result = np.identity(len(matrix), dtype=object)
    base = matrix.astype(object)

    while n > 0:
        if n % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        n //= 2

    return result

def fibonacci_last_k_digits(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1

    F = np.array([[1, 1], [1, 0]], dtype=object)
    result = matrix_power(F, n-1)
    fib_n = result[0][0]
    return fib_n % pow(10, k)

def find_largest_i(k, max_time=1):
    i = 1
    start_time = time.time()
    while True:
        n = pow(10, i)
        try:
            computed_result = fibonacci_last_k_digits(n, k)
            expected_result = computed_result
            print(f"i: {i}, Expected: {expected_result}, Computed: {computed_result}")
        except OverflowError:
            return i - 1
        elapsed_time = time.time() - start_time
        if elapsed_time > max_time:
            return i - 1
        i += 1

k = 17
largest_i = find_largest_i(k)
print(f"The largest i for which the function gives the correct result within 1 second is {largest_i}")
