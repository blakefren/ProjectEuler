import re
from itertools import combinations


class TrieNode:
    
    def __init__(self, value=None):
        self.value = value  # None if endpoint
        self.children = {}


class IntTrie:
    
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, integer:int):
        str_i = str(integer)
        current_node = self.root
        for char in str_i:
            if char not in current_node.children:
                current_node.children[char] = TrieNode(char)
            current_node = current_node.children[char]
        current_node.children[char] = TrieNode(None)  # Terminate

    def get_values_mask(self, mask:str, node:TrieNode=None):
        # Expect mask to be a string like '123*5' where the '*' is a wildcard.
        current_node = self.root if node is None else node
        values = []

        for i in range(len(mask)):
            print(mask, i, mask[i:])
            if mask[i] == '*':  # Wildcard
                for child in current_node.children.keys():
                    print(child)
                    self.get_values_mask(mask=mask[i:], node=current_node.children[child])
            else:
                values = [val+mask[i] for val in values]
        
        return values


def prob_51(family_size):
    # O(n) solution.  # TODO
    
    # Generate primes up to some large number.
    n = 10**5  # 7
    print(f'\nGenerating primes up to {n}...\n')
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
    
    # Split primes to dict entries based on number of digits.
    prime_dict = {i+1:{} for i in range(len(str(n))-1)}
    for p in primes:
        prime_dict[len(str(p))][p] = True
    del primes

    # TODO: would this be easier with a trie?
    # https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
    
    # Create and populate a trie with string representations of all primes.
    print(f'Inserting primes to trie...')
    trie = IntTrie()
    for l in prime_dict.keys():
        for p in prime_dict[l].keys():
            trie.insert(p)
    
    # Loop through all patterns and primes.
    print(f'Generating patterns and matching primes to patterns...')
    memo_patterns = {}
    for length in range(1, len(str(n))-1):

        for num_wildcards in range(1, length):

            if num_wildcards == 1:  # TEMP
                continue  # TEMP

            print(f'Checking primes of length {length} with {num_wildcards} wildcards')  # TEMP?

            combs = combinations(list(range(length)), min(length, num_wildcards))

            for positions in combs:
                
                print(positions)  # TEMP

                for i, prime in enumerate(prime_dict[length].keys()):
                    
                    str_prime = str(prime)
                    for j in positions:
                        str_prime = str_prime[:j] + '*' + str_prime[j+1:]

                    if str_prime in memo_patterns:
                        continue
                    memo_patterns[str_prime] = True

                    trie.get_values_mask(str_prime)

                    exit()  # TEMP

                    print(i, positions, positions[1:len(positions)])  # TEMP

                    for j in positions[1:len(positions)]:
                        print('found it', j, positions, prefixes)
                        # prefixes.append
                    
                    break  # TEMP
                break  # TEMP
            break  # TEMP

    return None


if __name__ == '__main__':
    # Answer: 
    print(prob_51(6))  # 8
