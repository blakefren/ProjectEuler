def prob_14(n):
    # O(n*c) solution, where n is the highest number to check and c is the average chain length.
    
    longest_chain = -1
    max_i = 1

    for i in range(2, n):
        
        current_num = i
        current_chain = 0

        while current_num > 1:
            if current_num % 2 == 0:
                current_num /= 2
            else:
                current_num = current_num*3 + 1
            current_chain += 1
        
        if current_chain > longest_chain:
            max_i = i
            longest_chain = current_chain
    
    return max_i


if __name__ == '__main__':
    # Answer: 837799
    print(prob_14(1000000))
