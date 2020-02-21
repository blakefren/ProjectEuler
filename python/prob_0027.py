def prob_27(max_range):
    # O(m*n) solution, where m is the max range and n is the max generatd prime number.
    
    # Generate primes.
    upper_prime = 10**5
    nums = [True for _ in range(upper_prime+1)]
    nums[0] = False
    nums[1] = False
    for i in range(upper_prime+1):
        if nums[i]:  # If prime, get rid of all multiples.
            for j in range(2, upper_prime//i+1):
                nums[i*j] = False
    primes = {i:{} for (i, prime) in enumerate(nums) if prime}
    sorted_primes = list(sorted(primes.keys()))
    del nums

    # test values for [n^2 + an + b] where
    # a between (exclusive) -1000 and 1000 and
    # b between (incusive) -1000 and 1000
    # but - b must be a positive prime for n=0 case
    max_prime_count = 0
    best_a = 0
    best_b = 0
    for a in range(-max_range+1, max_range):
        for b in sorted_primes:
            if b > max_range:
                break
            n = 0
            while (n**2 + a*n + b) in primes:
                n += 1
            if n > max_prime_count:
                max_prime_count = n
                best_a = a
                best_b = b
                
    return best_a*best_b


if __name__ == '__main__':
    # Answer: -59231
    print(prob_27(1000))
