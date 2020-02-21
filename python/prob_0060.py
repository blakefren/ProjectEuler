from itertools import combinations
from math import factorial

def prob_60(set_size, upper_prime=10**6):
    # O(p*s*n^2) solution where p is the number of primes less than upper_prime,
    # s is the set_size, and n is the avg number of pairs for each prime.
    
    # Generate primes up to some large number. O(p)
    nums = [True for _ in range(upper_prime+1)]
    nums[0] = False
    nums[1] = False
    for i in range(upper_prime+1):
        if nums[i]:  # If prime, get rid of all multiples.
            for j in range(2, upper_prime//i+1):
                nums[i*j] = False
    primes = {str(i):{} for (i, prime) in enumerate(nums) if prime}
    del nums

    # Generate all prime pairs, starting with the largest prime,
    # find every possible concatenated pair of primes. O(p*log(p))
    for p in reversed(sorted(primes.keys())):
        for split_index in range(1, len(p)):
            a = p[:split_index]
            b = p[split_index:]
            if a in primes and b in primes:
                if b not in primes[a]:
                    primes[a][b] = []
                primes[a][b].append(p)
                if a not in primes[b]:
                    primes[b][a] = []
                primes[b][a].append(p)
    
    # Filter to primes valid for our criteria. O(p*n)
    expected_perms = factorial(set_size)//factorial(set_size-2)//2
    valid_primes = {}
    for p in primes.keys():

        # Initial filter.
        if len(primes[p]) < expected_perms:
            continue

        # Remove any prime matches that did not have a reverse concat match.
        delete_keys = []
        for a in primes[p].keys():
            if len(primes[p][a]) != 2:
                delete_keys.append(a)
                continue
        for k in delete_keys:
            del primes[p][k]

        # Final filter.
        if len(primes[p]) < expected_perms:
            continue
        valid_primes[p] = primes[p]
    del primes
    
    # Check that each one of the paired primes has all the other pairs,
    # and find the group with the lowest sum. O(p*s*n^2)
    lowest_sum = upper_prime*set_size*10
    memo_combs = {}
    for int_p in reversed(sorted(map(int, valid_primes.keys()))):  # Start with larger values.

        p = str(int_p)
        num_valid = len(valid_primes[p].keys())
        num_combs = factorial(num_valid)//factorial(num_valid-(set_size-1))//factorial(set_size-1)
        if num_combs > (upper_prime//10**2):
            continue
        combs = combinations(list(valid_primes[p].keys()), set_size-1)
        
        for comb in combs:

            prime_group = tuple(list(comb) + [p])
            if prime_group in memo_combs:
                continue
            memo_combs[prime_group] = True

            invalid_prime = False
            for prime in prime_group:
                if prime not in valid_primes:
                    invalid_prime = True
                    break
            if invalid_prime:
                continue
            
            continue_break = False
            for prime1 in prime_group:
                for prime2 in prime_group:
                    if prime1 == prime2:
                        continue
                    if prime2 not in valid_primes[prime1]:
                        continue_break = True
                        break
                
                if continue_break:
                    break

            if continue_break:
                continue

            if sum(map(int, prime_group)) < lowest_sum:
                lowest_sum = sum(map(int, prime_group))

    return lowest_sum


if __name__ == '__main__':
    # Answer: 26033
    print(prob_60(5, 10**8))
