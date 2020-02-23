def prob_40(max_ten_power):
    # O(n) solution.

    # Brute force method.
    product = 1
    concat = ''.join(str(_) for _ in range(1, 10**(max_ten_power-1)))

    for i in range(max_ten_power):
        product *= int(concat[10**i-1])
    
    return product
    

if __name__ == '__main__':
    # Answer: 210
    print(prob_40(7))
