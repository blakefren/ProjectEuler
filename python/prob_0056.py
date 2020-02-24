def prob_56(n):
    # O(n^2*log(n)) solution.

    max_sum = -1

    for a in range(1, 100):
        for b in range(1, 100):
            digit_sum = sum([int(i) for i in str(a**b)])
            max_sum = max(max_sum, digit_sum)
    
    return max_sum


if __name__ == '__main__':
    # Answer: 972
    print(prob_56(100))
