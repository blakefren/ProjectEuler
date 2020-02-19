import math

def prob_24(n):
    # O(1) solution.
    
    digits = [0, 1, 2 , 3, 4, 5, 6, 7, 8, 9]
    assert n <= math.factorial(len(digits))

    # We can create the permutation without generating all of them and counting.
    # We can use the given position and the fact that it's ordered.

    factorial_rep = []
    for i in reversed(range(len(digits))):
        i_fac = math.factorial(i)
        factorial_rep.append(n//i_fac)
        n = n%i_fac

    perm = ''
    for f in factorial_rep:
        perm += str(digits.pop(f))
    
    return perm


if __name__ == '__main__':
    # Answer: 2783915604
    print(prob_24(1000000))
