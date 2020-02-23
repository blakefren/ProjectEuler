def prob_45():
    # Linear time solution, with O(1) memory.

    t_index = 285 + 1
    p_index = 165 + 1
    h_index = 143 + 1

    while True:

        t = t_index * (t_index + 1) // 2
        p = p_index * (3*p_index - 1) // 2
        h = h_index * (2*h_index - 1)

        if t == p == h:
            return t
        elif p < t:
            p_index += 1
        elif h < t:
            h_index += 1
        elif t < p or t < h:
            t_index += 1


if __name__ == '__main__':
    # Answer: 1533776805
    print(prob_45())
