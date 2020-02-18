def prob_7(n):
    # O(n*p) solution, where p is the number of primes less than n.
    
    primes = [2, 3]
    i = 4

    while len(primes) != n:

        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)
        
        i += 1

    return primes[n-1]


if __name__ == '__main__':
    # Answer: 104743
    print(prob_7(10001))
