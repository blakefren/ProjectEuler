def prob_35(n):
    # O(n*log(n)) solution.
    
    # Generate primes up to n.
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

    # Check each prime for circularity.
    count = 0
    for prime in primes.keys():
        str_prime = str(prime)
        circular = True
        for position in range(1, len(str_prime)):
            if int(str_prime[position:] + str_prime[:position]) not in primes:
                circular = False
                break
        if circular:
            count += 1

    return count


if __name__ == '__main__':
    # Answer: 
    print(prob_35(10**6))
