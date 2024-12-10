import random as rnd

def fermat_check(n):
    if (n == 2 or n == 3):
        return True
    elif n < 2:
        return False
    for i in range(30):
        a = rnd.randint(2, n-1)
        result = pow(a, n-1, n)
        if result != 1:
            return False
    return True


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


num = int("58.094.662.081".replace('.', ''))  
print(num)  
print(f"Fermat primality test result for {num}: {'likely prime' if fermat_check(num) else 'composite'}")
print(f"Miller-Rabin primality test result for {num}: {'likely prime' if miller_rabin(num) else 'composite'}")