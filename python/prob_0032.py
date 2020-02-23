def prob_32():
    # O(1) solution, since there is no input?

    pandigital_prods = {}

    for i in range(2, 10**2):
        
        # If a digit occurs more than once in i, skip.
        str_i = str(i)
        if '0' in str_i or not pandigital_check(i):
            continue
        
        j = 2  # Can't have solutions where j=1 since a*1=a
        str_j = str(j)
        while True:

            if len(str_i) + len(str_j) + len(str(i*j)) < 9:
                j += 1
                str_j = str(j)
                continue
            elif len(str_i) + len(str_j) + len(str(i*j)) > 9:
                break
            
            # If a digit occurs more than once in i, skip.
            if '0' in str_j or not pandigital_check(j):
                j += 1
                str_j = str(j)
                continue
            
            # Check "pandigital-ness" of str(i) + str(j) + str(i*j)
            ij = i*j
            str_ij = str(ij)
            if '0' in str_ij or not pandigital_check(str_i + str_j + str_ij):
                j += 1
                str_j = str(j)
                continue
            else:
                pandigital_prods[ij] = True

            j += 1
            str_j = str(j)
        
    return sum(pandigital_prods.keys())


def pandigital_check(n):

    last_char = 'a'
    pandigital = True
    for char in sorted(str(n)):
        if char == last_char:
            pandigital = False
            break
        last_char = char
    
    return pandigital


if __name__ == '__main__':
    # Answer: 
    print(prob_32())
