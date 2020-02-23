def prob_37():
    # O(n) solution.
    
    # Generate primes up to n.
    n = 10**6
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(n):
        if not primes[i]:
            continue
        j = 2
        while i*j < n:
            primes[i*j] = False
            j += 1
    primes = {i:True for i, prime in enumerate(primes) if prime}

    prime_sum = 0
    for prime in primes.keys():
        str_prime = str(prime)
        truncatable = True
        for i in range(1, len(str_prime)):
            if int(str_prime[i:]) not in primes or int(str_prime[:i]) not in primes:
                truncatable = False
        if truncatable and len(str_prime) > 1:
            prime_sum += prime
    
    return prime_sum


if __name__ == '__main__':
    # Answer: 748317
    print(prob_37())
