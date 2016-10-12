# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by Fu Zheng and Eric Martin for COMP9021


import sys
from random import seed, randint

from array_queue import *


dim = 10
grid = [[0] * dim for i in range(dim)]
queue = ArrayQueue()

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()

def seek():
    temp = queue.dequeue()
    print('temp', temp[-1][0])
    i = int(temp[-1][0])
    j = int(temp[-1][1])
    if i == 0:
        if j == 0:
            if grid[i + 1][j] == 0 and grid[i][j + 1] == 0:
                return
        if j == dim - 1:
            if grid[i + 1][j] == 0 and grid[i][j - 1] == 0:
                return
        if grid[i + 1][j] == 0 and grid[i][j + 1] == 0 and grid[i][j - 1] == 0:
            return
    if i == dim - 1:
        if j == 0:
            if grid[i - 1][j] == 0 and grid[i][j + 1] == 0:
                return
        if j == dim - 1:
            if grid[i - 1][j] == 0 and grid[i][j - 1] == 0:
                return
        if grid[i - 1][j] == 0 and grid[i][j + 1] == 0 and grid[i][j - 1] == 0:
            return
    if j == 0:
        if grid[i - 1][j] == 0 and grid[i][j + 1] == 0 and grid[i + 1][j] == 0:
            return
    if j == dim - 1:
        if grid[i - 1][j] == 0 and grid[i][j - 1] == 0 and grid[i + 1][j] == 0:
            return
    if grid[i - 1][j] == 0 and grid[i][j - 1] == 0 and grid[i + 1][j] == 0 and grid[i][j + 1] == 0:
        return
    
    print('temp', i, j)
    if i < dim and grid[i + 1][j]:
        queue.enqueue(temp.append((i + 1, j)))
        grid[i + 1][j] = 0
    if j < dim and grid[i][j + 1]:
        queue.enqueue(temp.append((i, j+1)))
        grid[i][j + 1] = 0
    if i > 0 and grid[i - 1][j]:
        queue.enqueue(temp.append((i - 1, j)))
        grid[i - 1][j] = 0
    if j > 0 and grid[i][j - 1]:
        queue.enqueue(temp.append((i, j-1)))
        grid[i][j - 1] = 0
    print('check ', queue.is)
    seek()

def leftmost_longest_path_from_top_left_corner():
    i = 0
    j = 0
    if not grid[i][j]:
        return
    
    grid[i][j] = 0
    queue.enqueue([(i, j)])
    return seek()

provided_input = input('Enter one integer: ')
try:
    seed_arg = int(provided_input)
except:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/2 to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = randint(0, 1)
print('Here is the grid that has been generated:')
display_grid()

path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner')
else:
    print('The leftmost longest path from the top left corner is {}'.format(path))
           
