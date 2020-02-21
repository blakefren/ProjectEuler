from decimal import Decimal, getcontext


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(len(lst), 0, -n):
        yield lst[max(0, i-n):i]


def prob_26(n):
    # O(n) solution.
    getcontext().prec = 100  # TODO

    max_pattern_repeat = 0

    for i in range(1, n):

        if i != 7:  # TEMP
            continue  # TEMP

        fraction = str(1 / Decimal(i))[2:]
        fraction_len = len(fraction)
        print(fraction)  # TEMP

        for j in reversed(range(1, fraction_len//2)):

            pattern = fraction[fraction_len//2+j:fraction_len]
            print(pattern)  # TEMP
            for chunk in chunks(fraction, len(pattern)):
                print(pattern, len(pattern), chunk, len(chunk))  # TEMP
                # break  # TEMP
            # TODO: run the pattern check
            
            # if full_pattern_match:
                # max_pattern_repeat = max(max_pattern_repeat, len(pattern))
            
            # break  # TEMP
        break  # TEMP
    
    return max_pattern_repeat


if __name__ == '__main__':
    # Answer: 
    print(prob_26(1000))
