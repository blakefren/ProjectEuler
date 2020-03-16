from itertools import permutations

def prob_62(num_perms):
    # O(n) solution, where n is ____.
    
    # Generate cubes up to some number.
    n = 10**4
    cubes = {str(i**3):{str(i**3):True} for i in range(n)}
    print(f'cubes complete')

    # Check each cube for its permutations.
    # Brute force solution.
    for cube in sorted(cubes.keys()):  # O(n)
        
        # if cube != '41063625':
            # continue

        perms = permutations(cube)
        count = 1

        for p in perms:  # O(log(n)!)
            if ''.join(p) in cubes and ''.join(p) not in cubes[cube]:
                count += 1
                cubes[cube][''.join(p)] = True
        
        if count == num_perms:
            return int(cube)


if __name__ == '__main__':
    # Answer: ____
    print(prob_62(3))
