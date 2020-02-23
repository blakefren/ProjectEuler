def prob_20(n):
    # O(n) solution.
    
    fact = 1
    for i in range(1, n+1):
        fact *= i
    
    return sum([int(d) for d in str(fact)])


if __name__ == '__main__':
    # Answer: 648
    print(prob_20(100))
