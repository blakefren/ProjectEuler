import re
from itertools import permutations


def prob_51(family_size):
    # O(n) solution.
    
    # Generate primes up to some large number.
    n = 10**6
    print(f'\nGenerating primes up to {n}...\n')
    primes = [2]
    for i in range(3, n, 2):  # Skip evens.
        prime = True
        for p in primes:
            if i%p==0:
                prime = False
        if prime:
            primes.append(i)

    # Split primes to dict entries based on number of digits.
    prime_dict = {i+1:[] for i in range(len(str(n))-1)}
    for p in primes:
        prime_dict[len(str(p))].append(str(p))  # For regex matching later.
    del primes

    # TODO: would this be faster with a trie?
    # Just find branches that are family_size in length.
    # https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python

    # Create patterns based on number of digits and wildcards to include.
    memo_patterns = {}
    for length in prime_dict.keys():
        
        for num_wildcards in range(1, length):
            
            print(f'Checking primes of len {length} with {num_wildcards} wildcard(s)...')

            places = list(range(length))
            perms = permutations(places, min(length, num_wildcards))
            
            for wildcard_pos in perms:

                # Check each prime pairing, starting with the smaller one.
                for i in range(len(prime_dict[length])):

                    # Build the regex.
                    reg = list(prime_dict[length][i])
                    wildcard_pos = sorted(wildcard_pos)
                    reg[wildcard_pos[0]] = '(.)'
                    for pos in wildcard_pos[1:]:
                        reg[pos] = r'(\1)'  # Match first group match (same digit).
                    reg = ''.join(reg)

                    # Check if we've run this pattern before.
                    if reg in memo_patterns:
                        continue
                    else:
                        memo_patterns[reg] = True

                    # Check regex against starting prime.
                    if not re.match(reg, prime_dict[length][i]):
                        continue
                    
                    # Compare regex against all larger primes with same number of digits.
                    match_set = [prime_dict[length][i]]
                    for j in range(i+1, len(prime_dict[length])):
                        if re.match(reg, prime_dict[length][j]):
                            match_set.append(prime_dict[length][j])
                
                    if len(match_set) >= family_size:
                        return match_set, reg  # TEMP (reg)
    
    return None


if __name__ == '__main__':
    # Answer: 
    print(prob_51(8))
