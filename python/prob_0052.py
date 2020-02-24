def prob_52(n):
    
    i = 1
    while True:
        nums = [i*j for j in range(1, n+1)]
        str_nums = [sorted(str(k)) for k in nums]
        if str_nums.count(str_nums[0]) == len(str_nums):
            return i
        i += 1


if __name__ == '__main__':
    # Answer: 142857
    print(prob_52(6))
