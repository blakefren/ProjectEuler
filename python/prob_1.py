def prob_1():
    '''
    Answer: 233168
    '''
    
    sum = 0
    for i in xrange(1000):
        if i%3==0 or i%5==0:
            sum += i
    return sum


if __name__ == '__main__':
    print(prob_1())
