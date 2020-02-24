def prob_55(max_num):
    # O(n*log(n)) solution.
    
    lychrel_count = 0
    for i in range(1, max_num+1):

        current_num = i
        palindromic = False

        for _ in range(50):
            current_num = current_num + int(str(current_num)[::-1])
            str_num = str(current_num)
            if str_num == str_num[::-1]:
                palindromic = True
                break

        if not palindromic:
            lychrel_count += 1
    
    return lychrel_count



if __name__ == '__main__':
    # Answer: 249
    print(prob_55(10000))
