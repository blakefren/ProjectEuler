from itertools import permutations


def prob_49():
    
    # Generate primes to n.
    n = 10**4
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(n):
        if not primes[i]:
            continue
        j = 2
        while i*j < n:
            primes[i*j] = False
            j += 1
    primes = {i:False for i, prime in enumerate(primes) if (prime and len(str(i))==4)}

    # Check permutations of each prime for the sequence.
    for prime in primes.keys():
        
        if primes[prime]:  # Already checked this value.
            continue
        
        primes[prime] = True
        sequence = {prime:True}
        
        for perm in permutations(str(prime)):  # 4! permutations per prime
            int_perm = int(''.join(perm))
            if int_perm in primes:
                sequence[int_perm] = True
                primes[int_perm] = True
        
        if len(sequence.keys()) < 3:
            continue

        if 1487 in sequence:  # Need to skip this solution
            continue
        
        sequence = list(sorted(sequence.keys()))
        for i in range(len(sequence)):
            for j in range(i+1, len(sequence)):
                if 2*sequence[j] - sequence[i] in sequence:
                    return str(sequence[i]) + str(sequence[j]) + str(2*sequence[j]-sequence[i])


if __name__ == '__main__':
    # Answer: 296962999629
    print(prob_49())
