def prob_36(n):
    # O(n*log(n)) solution.
    
    total_sum = 0
    for i in range(n):

        # Check that decimal is palindromic.
        decimal = False
        if i == int(str(i)[::-1]):
            decimal = True

        # Check that binary is palindromic.
        binary = False
        bin_num = format(i, 'b')
        if bin_num == str(bin_num)[::-1]:
            binary = True

        if decimal and binary:
            total_sum += i

    return total_sum


if __name__ == '__main__':
    # Answer: 872187
    print(prob_36(10**6))
