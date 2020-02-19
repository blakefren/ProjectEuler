def prob_23(limit):
    # O(n^2) solution where n is the upper limit.
    
    # Generate all abundant numbers beneath the limit.
    abundant_nums = []
    for i in range(1, limit+1):
        i_sum = 0
        j = 1
        while j*j <= i:
            if i%j==0:
                i_sum += j
                i_sum += i//j if j*j!=i else 0
            j += 1
        i_sum -= i
        if i_sum > i:
            abundant_nums.append(i)

    # Compile a list of all numbers that are the sum of two abundant nums.
    sum_nums = {}
    for i, num1 in enumerate(abundant_nums):  # These two loops are O(n^2).
        for j, num2 in enumerate(abundant_nums[i:]):
            if num1+num2 < limit+1:  # No need to store numbers above the limit.
                sum_nums[num1+num2] = True
    
    # Return the sum of the numbers not in the above list.
    abundant_sum = 0
    for i in range(1, limit+1):
        if i not in sum_nums:
            abundant_sum += i

    return abundant_sum


if __name__ == '__main__':
    # Answer: 4179871
    print(prob_23(28123))
