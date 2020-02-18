from math import factorial

def prob_15(n):
    # O(n) solution.
    
    # I need to count all permutations of n "right" and n "down" moves.
    # I can count this by using binomal coefficients (thanks Wolfram).
    return factorial(2*n) // factorial(n)**2


if __name__ == '__main__':
    # Answer: 137846528820
    print(prob_15(20))
