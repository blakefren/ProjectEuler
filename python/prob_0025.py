def prob_25(digits):
    # O(n) solution, where n is the number of digits requested.
    
    # Generate Fibonachi nums until we meet the criteria.
    fibs = [1, 1]
    index = 2
    while len(str(fibs[1])) != digits:
        fibs[1] = sum(fibs)
        fibs[0] = fibs[1] - fibs[0]
        index += 1

    return index


if __name__ == '__main__':
    # Answer: 4782
    print(prob_25(1000))
