def prob_2():
    '''
    Answer: 4613732
    '''

    fib_sum = 2
    a = 1
    b = 2
    current_sum = a+b
    while current_sum <= 4000000:
        if current_sum % 2 == 0:
            fib_sum += current_sum
        a = b
        b = current_sum
        current_sum = a + b
    return fib_sum


if __name__ == '__main__':
    print(prob_2())
