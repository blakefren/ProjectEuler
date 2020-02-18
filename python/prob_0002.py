def prob_2(n):
    # O(n) solution.

    fib_sum = 2
    a = 1
    b = 2
    current_sum = a+b
    while current_sum <= n:
        if current_sum % 2 == 0:
            fib_sum += current_sum
        a = b
        b = current_sum
        current_sum = a + b
    return fib_sum


if __name__ == '__main__':
    # Answer: 4613732
    print(prob_2(4000000))
