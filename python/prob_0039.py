from math import sqrt


def prob_39(p_max):
    # O(p^3) solution.
    
    max_solutions = 0
    best_p = -1

    for p in range(1, p_max+1):
        
        p_sols = {}
        for a in range(1, p//2):  # If one side is 1/2 the perimiter, can't make a triangle.
            for b in range(1, (p-a)//2+1):
                
                hypo = p-a-b
                if (a**2 + b**2) == hypo**2:
                    p_sols[tuple(sorted([a, b, hypo]))] = True
        
        if len(p_sols.keys()) > max_solutions:
            max_solutions = len(p_sols.keys())
            best_p = p

    return best_p
    

if __name__ == '__main__':
    # Answer: 840
    print(prob_39(1000))
