import os, sys


def prob_67(tree):
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
    # Answer: 7273
    tree = []
    with open(os.path.join(sys.path[0], 'p067_triangle.txt'), 'r') as f:
        for row in f.read().split('\n'):
            if row == '':
                continue
            tree.append(list(map(int, row.split(' '))))
    print(prob_67(tree))
