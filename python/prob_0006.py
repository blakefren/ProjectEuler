def prob_6(n):
    # O(n) solution.

    sum_squares = 0
    squared_sums = 0

    for i in range(n+1):
        sum_squares += i**2
        squared_sums += i

    return squared_sums**2 - sum_squares


if __name__ == '__main__':
    # Answer: 25164150
    print(prob_6(100))
