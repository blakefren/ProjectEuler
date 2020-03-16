def prob_63():
    # Brute force check for all numbers and powers below a threshold.

    count = 0
    for i in range(1, 10):
        for p in range(1, 10**2):
            power = i**p
            str_pow = str(power)
            if len(str_pow) == p:
                count += 1
            elif len(str_pow) > p:
                break

    return count


if __name__ == '__main__':
    # Answer: 49
    print(prob_63())
