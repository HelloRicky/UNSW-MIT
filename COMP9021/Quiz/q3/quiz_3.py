# Randomly fills an array of size 10x10 with 0s and 1s, and outputs the number of blocks
# in the largest block construction, determined by rows of 1s that can be stacked
# on top of each other. 
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


dim = 10


def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' 1', end = '') if grid[i][j] else print(' 0', end = '')
        print()
    print()


def size_of_largest_construction():
    maxVal = 0
    
    for i in range(dim, 0, -1):
        
        j1 = 0
        j2 = 0
        while j2 <= dim:
            if j2 < dim and grid[i-1][j2] :
                j2 += 1
                continue
            maxVal = max(maxVal, construction_size(i-1, j1, j2))
            j2 += 1
            j1 = j2
                
    return maxVal

# If j1 <= j2 and the grid has a 1 at the intersection of row i and column j
# for all j in {j1, ..., j2}, then returns the number of blocks in the construction
# built over this line of blocks.
def construction_size(i, j1, j2):
    sumVal = 0
    for col in range(j1, j2):
        lvl = i
        while grid[lvl][col] and lvl >= 0:
            
            sumVal += 1
            lvl -= 1
    return sumVal

            
try:
    for_seed, n = [int(i) for i in
                           input('Enter two integers, the second one being strictly positive: ').split()]
    if n <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(for_seed)
grid = [[randrange(n) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest block construction has {} blocks.'.format(size_of_largest_construction()))  
