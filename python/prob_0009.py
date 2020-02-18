def prob_9(n):
    # O(n^3) brute force solution, where n is the sum number.
    # o(n^2) more optimal solution.

    # Brute force method.
    '''for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                if a**2 + b**2 == c**2 and a+b+c == n:
                    return a*b*c'''

    # More optimal method.
    # c = (a**2 + b**2)**0.5
    # c = n - a - b
    # then (a**2 + b**2) = (n-a-b)**2
    for a in range(1, n):
        for b in range(1, n):
            if (a**2 + b**2) == (n-a-b)**2:
                return a*b*(n-a-b)


if __name__ == '__main__':
    # Answer: 31875000
    print(prob_9(1000))
