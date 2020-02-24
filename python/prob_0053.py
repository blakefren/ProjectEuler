from math import factorial


def prob_53(target):
    # O(n) solution.
    
    # Brute force test.
    count = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            comb_count = factorial(n) // factorial(r) // factorial(n-r)
            if comb_count > target:
                print(n, r, comb_count)
                count += 1
    
    return count


if __name__ == '__main__':
    # Answer: 4075
    print(prob_53(10**6))
