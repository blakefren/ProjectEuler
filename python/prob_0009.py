def prob_9(n):
    '''
    Answer: 31875000
    '''

    # Brute force method.
    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if a**2 + b**2 == c**2 and a + b + c == n:
                    return a*b*c


    # TODO: second method
    # c = (a + b) **2
    # c = n - a - b
    '''a = 1
    b = 1
    c = 1'''



if __name__ == '__main__':
    print(prob_9(1000))
