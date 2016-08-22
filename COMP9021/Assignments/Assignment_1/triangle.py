"""
COMP9021 Assignment 1
Task 2, Triangle
Created by: Fu Zheng
Created on: 12/08/2016
Version 2.0
"""
import os.path
from sys import exit

#-----------Initialise all variable below

q1 = "Which data file do you want to use?"
err1 = "Given file name doesn't exit in working directory!"
err2 = "Please give me a nonnegative integer!"
err3 = "Given file is empty."
msg1 = "The largest sum is:"
msg2 = "The number of paths yielding this sum is:"
msg3 = "The leftmost path yielding this sum is:"

array = []                      # array to store each digit of each row from the input txt file

#-----------Functions below

def checkFileExist(filename):
    """
    Return True if file exist in current working directory, else False
    """
    return os.path.isfile(filename)

def solve(tri):

    while len(tri) > 1:
        t0 = tri.pop()                          # extract last row
        t1 = tri.pop()                          # extract 2nd last row
        
        val = []                                # empty val for each row
        for i, t in enumerate(t1):
            new_val = []
            left = t0[i]
            right = t0[i + 1]
            maxVal = max(left[0], right[0]) + t # add the t value with max value of its leaf
            
            if left[0] == right[0]:             # if both equal, add up the possible path number
                temp = left[1][:]
                temp.append(t)
                new_val = [maxVal, temp, left[2] + right[2]]
            elif left[0] > right[0]:
                temp = left[1][:]
                temp.append(t)
                new_val = [maxVal, temp, left[2]]
            elif left[0] < right[0]:
                temp = right[1][:]
                temp.append(t)
                new_val = [maxVal, temp, right[2]]
                
            val.append(new_val)                 # generate new last row
        tri.append(val)                         # update triangle
        
    return tri[0][0]


#question 1

fname = input(q1)
ans1 = checkFileExist(fname)
while True:
    if ans1:
        break   
    print(err1)
    exit()

"""

Read input text file and store data to array

"""
with open(fname) as f:
    content = f.readlines()

# check if file is empty
if len(content) == 0:
    print(err3)
    exit()

for lines in content:
    lines.strip()
    array.append(list(map(int, lines.split()))) #append individual digit

"""
Update last Row format to [a_1, [a_2], a_3]

a_1 = current max sum of the path
a_2 = current max sum path
a_3 = current possible path total count, start from 1

e.g.

1
2 2
1 2 1

after reformat the last Row, it will be [[1, [1], 1], [2, [2], 1], [1, [1], 1]]

"""
lastRow = array.pop()
array.append(list(map(lambda i: [i, [i], 1], lastRow)))

result = solve(array)

#reverse leftmost path
result[1].reverse()

# output message:
print(msg1, result[0])
print(msg2, result[2])
print(msg3, result[1])

