from decimal import Decimal, getcontext

def prob_26(n):
    # O(n) solution.
    getcontext().prec = 100

    max_pattern_repeat = 0

    for i in range(1, n):
        fraction = str(1 / Decimal(i))[2:]
        fraction_len = len(fraction)

        for j in reversed(range(1, fraction_len//2)):
            pattern = fraction[fraction_len//2+j+1:fraction_len]

            # TODO: run the pattern check
    
    return max_pattern_repeat


if __name__ == '__main__':
    # Answer: 
    print(prob_26(1000))
