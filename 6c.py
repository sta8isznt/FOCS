import random as rnd

def miller_rabin(n, k=30):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = rnd.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def is_prime_mersenne(x):
    if not miller_rabin(x):
        return False
    mersenne = 2**x - 1
    return miller_rabin(mersenne)

def find_mersenne_primes(limit):
    mersenne_exponents = []
    for x in range(2, limit):
        if is_prime_mersenne(x):
            mersenne_exponents.append(x)
    return mersenne_exponents

mersenne_exponents = find_mersenne_primes(200)

print("Εκθέτες των πρώτων αριθμών Mersenne για 1 < x < 200:")
for exponent in mersenne_exponents:
    print(exponent)

official_mersenne_exponents = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127]

print("\nΣύγκριση με την επίσημη λίστα:")
for exponent in mersenne_exponents:
    if exponent in official_mersenne_exponents:
        print(f"{exponent} είναι σωστός")
    else:
        print(f"{exponent} δεν είναι στη λίστα")


