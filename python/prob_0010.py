def prob_10(n):
    # O(n*p) solution, where n is the max number and p is the number of primes less than n.
    # O(n) space complexity.

    # Sieve of Eratosthenes method. Brute force is too slow.
    nums = {i:False for i in range(2, n)}
    running_sum = 0

    for i in sorted(nums.keys()):
        
        if nums[i]:  # Already accounted for - not prime.
            continue
        running_sum += i
        # Mark all multiples of this value.
        j = 2
        while i*j < n:
            nums[i*j] = True
            j += 1
    
    return running_sum


if __name__ == '__main__':
    # Answer: 142913828922
    print(prob_10(2000000))
