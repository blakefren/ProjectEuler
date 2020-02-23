def prob_31(pounds):
    # O(n) solution.
    
    # Coins: 1, 2, 5, 10, 20, 50, 100, 200
    num_combs = 0
    pounds *= 100  # Change to pence

    # Brute force method - it's fast enough.
    for p200 in range(0, pounds+1, 200):
        for p100 in range(p200, pounds+1, 100):
            for p50 in range(p100, pounds+1, 50):
                for p20 in range(p50, pounds+1, 20):
                    for p10 in range(p20, pounds+1, 10):
                        for p5 in range(p10, pounds+1, 5):
                            for p2 in range(p5, pounds+1, 2):
                                num_combs += 1
            
    return num_combs


if __name__ == '__main__':
    # Answer: 73682
    print(prob_31(2))
