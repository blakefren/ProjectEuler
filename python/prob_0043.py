from itertools import combinations
from sys import maxsize

def prob_44():
    # O(n) solution.
    
    # Generate n pentagonal numbers.
    n = 10000
    pentagons = {i*(3*i-1)//2:True for i in range(1, n)}

    # Check all permutation pairs for the desired property.
    min_diff = maxsize
    for c in combinations(pentagons.keys(), 2):
        if (c[0]+c[1]) in pentagons and abs(c[0]-c[1]) in pentagons:
            min_diff = min(min_diff, abs(c[0]-c[1]))
    
    return min_diff


if __name__ == '__main__':
    # Answer: 5482660
    print(prob_44())
