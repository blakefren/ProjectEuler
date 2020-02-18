def prob_5(n):
    # O(n^2) solution.
    
    primes = {}

    # Get the prime factors of all numbers up to n, then multiply them and return.
    for i in range(2, n+1):

        num = i
        j = 2

        while j <= num:

            # Reduce num by this prime as many times as possible.
            count = 0
            while num % j == 0:
                count += 1
                num //= j
            
            primes[j] = max(primes.get(j, 0), count)

            # Find the next largest factor (should be a prime number).
            while num % j != 0 and j <= num:
                j += 1

    mult_num = 1
    for p in primes.keys():
        mult_num *= p ** primes[p]
    
    return mult_num


if __name__ == '__main__':
    # Answer: 232792560
    print(prob_5(20))
