import re
from itertools import permutations


class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}


def prob_51(family_size):
    # O(n) solution.
    
    # Generate primes up to some large number.
    n = 10**3
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
    '''prime_dict = {i+1:[] for i in range(len(str(n))-1)}
    for p in primes:
        prime_dict[len(str(p))].append(str(p))  # For regex matching later.
    del primes'''

    # TODO: would this be easier with a trie?
    # https://stackoverflow.com/questions/11015320/how-to-create-a-trie-in-python
    
    # Create and populate a trie with string representations of all primes.
    root = TrieNode('')
    for p in primes:
        current_node = root
        for digit in str(p):
            current_node = current_node.children.setdefault(digit, TrieNode(digit))
    
    # Loop through all primes.
    for p in primes:


    # print(root.children['9'].children['7'].children['1'].children)

    return None


if __name__ == '__main__':
    # Answer: 
    print(prob_51(8))
