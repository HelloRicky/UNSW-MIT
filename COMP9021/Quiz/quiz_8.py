# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, randint

from array_queue import *


dim = 10
grid = [[0] * dim for i in range(dim)]

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()

def leftmost_longest_path_from_top_left_corner():
    queue=ArrayQueue()
    anw={}
    if grid[0][0]:
        queue.enqueue([(0,0)])
        if grid[0][1] or grid[1][0]:
            temp=queue.dequeue()
            if grid[0][1]:
                queue.enqueue(temp+[(0,1)])
            if grid[1][0]:
                queue.enqueue(temp+[(1,0)])
        else:
            return queue.dequeue()
    else: return None
    while not queue.is_empty():
        branch=queue.dequeue()
        b=branch[-1]
        i=b[0]
        j=b[1]
        flag=0
        a=branch[-2]
        if a[0]==b[0] and a[1]==b[1]-1:      
            if i-1>-1 and (i-1,j)not in branch and grid[i-1][j]:
                queue.enqueue(branch+[(i-1,j)])
                flag=1
            if j+1<10 and grid[i][j+1] and (i,j+1)not in branch:
                queue.enqueue(branch+[(i,j+1)])
                flag=1
            if i+1<10 and grid[i+1][j]and (i+1,j)not in branch:
                queue.enqueue(branch+[(i+1,j)])
        elif a[0]==b[0]-1 and a[1]==b[1]:
            if j+1<10 and grid[i][j+1] and (i,j+1)not in branch:
                queue.enqueue(branch+[(i,j+1)])
                flag=1
            if i+1<10 and grid[i+1][j]and (i+1,j)not in branch:
                queue.enqueue(branch+[(i+1,j)])
                flag=1
            if j-1>-1 and ((i,j-1)not in branch) and grid[i][j-1]:
                queue.enqueue(branch+[(i,j-1)])
                flag=1
        elif a[0]==b[0] and a[1]==b[1]+1:
            if i+1<10 and grid[i+1][j]and (i+1,j)not in branch:
                queue.enqueue(branch+[(i+1,j)])
                flag=1
            if j-1>-1 and ((i,j-1)not in branch) and grid[i][j-1]:
                queue.enqueue(branch+[(i,j-1)])
                flag=1
            if i-1>-1 and ((i-1,j)not in branch) and grid[i-1][j]:
                queue.enqueue(branch+[(i-1,j)])
                flag=1  
        elif a[0]==b[0]+1 and a[1]==b[1]:
            if j-1>-1 and ((i,j-1)not in branch) and grid[i][j-1]:
                queue.enqueue(branch+[(i,j-1)])
                flag=1
            if i-1>-1 and ((i-1,j)not in branch) and grid[i-1][j]:
                queue.enqueue(branch+[(i-1,j)])
                flag=1
            if j+1<10 and grid[i][j+1] and (i,j+1)not in branch:
                queue.enqueue(branch+[(i,j+1)])
                flag=1     
        if flag==0:
            a=len(branch)
            if a in anw:
                anw[a].append(branch)
            else:anw[a]=([branch])
        flag=0
    maxkey=max(anw.keys())
    l=[]
    l=(anw.get(maxkey))
    return(l[0])
            

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
           
