def prob_18(tree):
    # O(n*log(n)) solution, where n is the tree depth.
    # Each node is only touched 3 times, except for the root and bottom row.
    
    # Need to calculate the results from each node down in place.
    # Start at the bottom and working our way up.
    # Then, we just need to select the result from the top of the tree.

    for row in reversed(range(len(tree)-1)):  # Skip last row.
        for col in range(len(tree[row])):
            a = tree[row][col] + tree[row+1][col]
            b = tree[row][col] + tree[row+1][col+1]
            tree[row][col] = max(a, b)
    
    return tree[0][0]


if __name__ == '__main__':
    # Answer: 
    tree = ['75',
        '95 64',
        '17 47 82',
        '18 35 87 10',
        '20 04 82 47 65',
        '19 01 23 75 03 34',
        '88 02 77 73 07 63 67',
        '99 65 04 28 06 16 70 92',
        '41 41 26 56 83 40 80 70 33',
        '41 48 72 33 47 32 37 16 94 29',
        '53 71 44 65 25 43 91 52 97 51 14',
        '70 11 33 28 77 73 17 78 39 68 17 57',
        '91 71 52 38 17 14 91 43 58 50 27 29 48',
        '63 66 04 68 89 53 67 30 73 16 69 87 40 31',
        '04 62 98 27 23 09 70 98 73 93 38 53 60 04 23']
    clean_tree = [list(map(int, row.split(' '))) for row in tree]
    print(prob_18(clean_tree))
