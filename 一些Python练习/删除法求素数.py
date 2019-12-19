def prime(n):
    primes = list(range(2, n + 1))
    for p in primes:
        if p * p > n:
            break
        product = 2 * p
        while product <= n:
            if product in primes:
                primes.remove(product)
            product += p
    return len(primes), primes


print(prime(100))
