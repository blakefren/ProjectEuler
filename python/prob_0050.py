from collections import OrderedDict, deque


def prob_20(n):
    # O(n^2) solution.
    
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
    primes = [i for i, prime in enumerate(primes) if prime]
    prime_dict = {i:True for i in primes}

    # Check for the highest prime that matches the sum.
    highest_terms = 0
    highest_prime = 0
    for i in range(len(primes)):

        running_sum = primes[i]
        num_terms = 1
        for j in range(i+1, len(primes)):
            
            running_sum += primes[j]
            num_terms += 1

            # Early stopping for performance.
            if running_sum > primes[len(primes)-1]:
                break

            if running_sum in prime_dict and num_terms > highest_terms:
                highest_terms = num_terms
                highest_prime = running_sum

    return highest_prime, highest_terms


if __name__ == '__main__':
    # Answer: 997651
    print(prob_20(10**6))
