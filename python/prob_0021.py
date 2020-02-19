def prob_21(n):
    # O(n*sqrt(n)) solution.
    
    # Create dict of all sums up to n.
    sum_dict = {}
    for i in range(1, n):
        j = 1
        temp_sum = 0
        while j*j < i:
            if i%j==0:
                temp_sum += j
                temp_sum += i//j
            j += 1
        temp_sum -= i
        if i != temp_sum:
            sum_dict[i] = temp_sum
    
    # Check all values in dict, add to sum, and return.
    final_sum = 0
    for key in sum_dict.keys():
        if key == sum_dict.get(sum_dict[key], -1):
            final_sum += key
    
    return final_sum


if __name__ == '__main__':
    # Answer: 31626
    print(prob_21(10000))
