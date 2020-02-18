def prob_4(num_digits):
    # O(n^2) brute force solution.
    
    largest_palindrome = -1
    max_num = 10**num_digits - 1
    min_num = 10**(num_digits-1) - 1
    a = max_num

    while a > min_num:

        b = max_num
        while b > min_num:
            
            n = str(a*b)
            b -= 1

            if n == n[::-1]:
                largest_palindrome = max(int(n), largest_palindrome)
        
        a -= 1

    return largest_palindrome


if __name__ == '__main__':
    # Answer: 906609
    print(prob_4(3))
