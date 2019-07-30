import math
def is_prime(n):
    if n < 2:
        return False
    is_prime = True
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt):
        if n%i ==0:
            is_prime = False
            break
    return is_prime

print(is_prime(13),is_prime(15),is_prime(12))
