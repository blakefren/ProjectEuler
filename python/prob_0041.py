def prob_41():
    
    # Generate primes up to n.
    n = 10**7
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(n):
        if not primes[i]:
            continue
        j = 2
        while i*j < n:
            primes[i*j] = False
            j += 1
    primes = [i for i, prime in enumerate(primes) if prime]
    
    # Check all primes for pandigitality.
    max_prime = -1
    for prime in primes:
        if pandigital_check(prime) and prime > max_prime:
            max_prime = prime
    
    return max_prime


def pandigital_check(n):

    nums = ''.join([str(i) for i in range(1, len(str(n))+1)])

    if ''.join(sorted(str(n))) != nums:
        return False

    return True


if __name__ == '__main__':
    # Answer: 7652413
    print(prob_41())
