def prob_4():
    '''
    Answer: 906609
    '''
    
    num = -1
    a = 999

    while a > 99:

        b = 999
        while b > 99:
            
            n = str(a*b)
            b -= 1

            if n == n[::-1]:
                num = max(int(n), num)

        
        a -= 1

    return num


if __name__ == '__main__':
    print(prob_4())
