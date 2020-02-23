from itertools import product
from math import factorial


def prob_34():
    # O(1) solution.
    
    # Since 9!=362880, we can ignore any numbers above ~9!*10 since
    # we are limited to the order of 9! We'll say less than 10**7.

    # Pre-sum numbers up to 1000. Without pre-sum, loop is pretty slow.
    fact_nums = [sum(factorial(int(char)) for char in str(i)) for i in range(1000)]
    total_sum = 0

    for num in range(3, 10**7):
        
        a = num
        num_sum = 0
        while a >= 1000:
            num_sum += fact_nums[a % 1000]  # Take last 3 digits
            a = a//1000   # Remove last 3 digits
        num_sum += fact_nums[a % 1000]  # Get value for final 3 digits

        if num_sum == num:
            total_sum += num
    
    return total_sum


if __name__ == '__main__':
    # Answer: 40730
    print(prob_34())
