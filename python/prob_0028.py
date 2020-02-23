def prob_28(max_side_length):
    # O(m) solution, where m is the max_side_length.
    
    total = 1
    last_val = 1
    for side_length in range(3, max_side_length+1, 2):
        for _ in range(4):  # One for each side of the square spiral.
            last_val += side_length - 1
            total += last_val
    
    return total


if __name__ == '__main__':
    # Answer: 669171001
    print(prob_28(1001))
