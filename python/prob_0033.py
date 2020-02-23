from math import gcd

def prob_33(digits):
    # O(10**2n) brute force solution.

    numerator = 1
    denominator = 1
    
    for j in range(10**(digits-1), 10**digits):
        for i in range(10**(digits-1), j):  # Only where i<j

            str_i = str(i)
            str_j = str(j)

            candidates = []
            for char in str_i:
                if char in str_j:
                    candidates.append(char)
            
            # Remove first instance of number in numerator and denominator.
            # TODO: if occuring more than once, need to loop through all positions.
            for c in candidates:
                temp_i = int(str_i.replace(c, '', 1))
                temp_j = int(str_j.replace(c, '', 1))
                if temp_j!=0 and i/j == temp_i/temp_j and not (i%10==0 and j%10==0):
                    numerator *= i
                    denominator *= j
    
    return denominator // gcd(numerator, denominator)


if __name__ == '__main__':
    # Answer: 100
    print(prob_33(2))
