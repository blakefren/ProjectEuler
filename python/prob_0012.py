def prob_12(n):
    # O(t^2) solution, where t is the number of triangular nums checked.
    
    i = 2
    while True:
        triangular_num = sum(range(i+1))

        # Count all factors.
        count = 0
        j = 1
        while j*j < triangular_num:
            if triangular_num % j == 0:
                count += 2  # Symmetry around the square root.
            j += 1
        if j*j == triangular_num:
            count +=1

        if count >= n:
            return triangular_num
        i += 1


if __name__ == '__main__':
    # Answer: 76576500
    print(prob_12(500))
