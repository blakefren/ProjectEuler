from collections import OrderedDict


def prob_46():
    
    # Generate primes to n.
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
    primes = OrderedDict((i, True) for i, prime in enumerate(primes) if prime)

    # Search prime/square space to look for a match for the conjecture, return when no match.
    i = 3
    while True:
        
        if i in primes:
            i += 2
            continue
        
        conjecture_match = False
        for p in primes.keys():
            
            if p > i:
                break
            square = 1
            
            while square*square < i:
                if p + 2*square*square == i:
                    conjecture_match = True
                    break
                square += 1

            if conjecture_match:
                break
        
        if conjecture_match:
            i += 2
        else:
            return i


if __name__ == '__main__':
    # Answer: 
    print(prob_46())
