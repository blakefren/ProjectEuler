import os, sys

def prob_22(filename):
    # O(n*log(n) + c) solution, where n is the number of names
    # and c is the total number of characters in the file.
    
    raw_names = None
    filename = os.path.join(sys.path[0], filename)
    with open(filename, 'r') as f:
        raw_names = f.read()
    
    names = raw_names.split(',')  # O(c)
    names = sorted([name[1:len(name)-1] for name in names])  # O(n*log(n))

    base = ord('A') - 1
    total_score = 0

    for i, n in enumerate(names):  # O(n*avg_len(n)) loop.
        name_score = 0
        for char in n:
            name_score += ord(char) - base
        total_score += (i+1)*name_score

    return total_score


if __name__ == '__main__':
    # Answer: 871198282
    print(prob_22(r'p022_names.txt'))
