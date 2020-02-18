def prob_3(n):
    # O(sqrt(n)) solution.
    
    largest_prime = 2
    i = largest_prime
    
    while i * i < n:

        # Reduce n by this prime as many times as possible.
        while n % i == 0:
            n /= i

        # Find the next largest factor (should be a prime number)
        while n % i != 0:
            i += 1

        largest_prime = i
    
    return largest_prime


if __name__ == '__main__':
    # Answer: 6857
    print(prob_3(600851475143))
