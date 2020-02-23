def prob_30(power):
    # O(n*log(n)) solution.
    
    total = 0
    for i in range(2, 10**6):
        str_i = str(i)
        sum_digits = 0
        for digit in str_i:
            sum_digits += int(digit)**power
        if i == sum_digits:
            total += i
    
    return total


if __name__ == '__main__':
    # Answer: 443839
    print(prob_30(5))
