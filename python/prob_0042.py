import os, sys


def prob_42():
    # O(w*l) solution where w is the number of words in the file and
    # l is the average word length.

    # Read and clean the file.
    words = []
    with open(os.path.join(sys.path[0], 'p042_words.txt'), 'r') as f:
        words = f.read().split(',')
    for i in range(len(words)):
        words[i] = words[i][1:len(words[i])-1].upper()  # Trim the quotation marks.

    # Create the triangular dict.
    base = ord('A') - 1
    triangle_nums = {}
    for i in range(1, 100):
        triangle_nums[i*(i+1)//2] = True
    
    # Check each word against the dict.
    word_count = 0
    for word in words:
        
        word_sum = 0
        for letter in word:
            word_sum += ord(letter) - base
        
        if word_sum in triangle_nums:
            word_count += 1

    return word_count


if __name__ == '__main__':
    # Answer: 

    print(prob_42())





