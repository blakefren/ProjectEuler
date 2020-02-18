def prob_1(n):
    # O(n) solution.
    
    sum = 0
    for i in range(n):
        if i % 3==0 or i % 5==0:
            sum += i
    return sum


if __name__ == '__main__':
    # Answer: 233168
    print(prob_1(1000))
