def prob_48(n):
    # O(n) solution.
    
    total_sum = str(sum([i**i for i in range(1, n+1)]))

    return int(total_sum[len(total_sum)-10:])


if __name__ == '__main__':
    # Answer: 9110846700
    print(prob_48(1000))
