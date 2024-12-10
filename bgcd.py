def bgcd(a, b):
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a

    if a % 2 == 0 and b % 2 == 0:
        return 2 * bgcd(a // 2, b // 2)
    elif a % 2 == 0:
        return bgcd(a // 2, b)
    elif b % 2 == 0:
        return bgcd(a, b // 2)
    else:
        return bgcd(min(a, b), abs(a - b) // 2)

def gcd_euclidean(a, b):
    while b:
        a, b = b, a % b
    return a


import random
import time

a, b = 3**200, 2**250

start_time = time.time()
bgcd(a, b)
binary_gcd_time = time.time() - start_time

start_time = time.time()
gcd_euclidean(a, b)
euclidean_gcd_time = time.time() - start_time

print(f"Binary GCD time for a = 3**200 and b = 2**250: {binary_gcd_time:.10f} seconds")
print(f"Euclidean GCD time for a = 3**200 and b = 2**250: {euclidean_gcd_time:.10f} seconds")
