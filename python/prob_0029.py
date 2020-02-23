def prob_29(n):
    # O(n^2) solution.
    
    comb_dict = {}
    for a in range(2, n+1):
        for b in range(2, n+1):
            comb_dict[a**b] = True
    
    return len(comb_dict.keys())


if __name__ == '__main__':
    # Answer: 9183
    print(prob_29(100))
