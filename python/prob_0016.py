def prob_16(n):
    # O(d) solution, where d is the number of digits in n.
    return sum([int(d) for d in str(n)])


if __name__ == '__main__':
    # Answer: 1366
    print(prob_16(2**1000))
