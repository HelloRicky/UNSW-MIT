"""
COMP9021 Assignment 1
Task 2, Triangle
Created by: Fu Zheng
Created on: 12/08/2016
Version 1.0
"""
import os.path
from sys import exit

#-----------Initialise all variable below

q1 = "Which data file do you want to use?"
q2 = "The largest sum is:"
err1 = "Given file name doesn't exit in working directory!!"
err2 = "Please give me a nonnegative integer!!"
msg1 = "The number of paths yielding this sum is:"
msg2 = "The leftmost path yielding this sum is:"

array = []                      # array to store each digit of each row from the input txt file
collected_list = []             # store all the ordered element from the triangle, from top to bottom, left to right
brk = "flag"                    # use flag to identify new path in the 'findChild' loop

start_index = 0                 # find the first flag index in the collected_list
base_list = []                  # based list as the first path
path_all = []                   # store all the possible path
path_new_sub = []               # store sub list of all childen item after each flag, will use it to update base_list


leftMost = False                # return True if the first leftMost path that meet the largest sum is found
path_count = 0                  # record the total number of pathes that meet the largest sum
leftMost_list = []              # initital output list
#-----------Functions below

def checkFileExist(filename):
    """
    Return True if file exist in current working directory, else False
    """
    return os.path.isfile(filename)

def findChild(root, index, lvl):

    """
    root: current digit in current row
    index: root's position in current row
    lvl: child level of root (e.g. current lvl + 1)

    ---- debug code ---------
    print("current root", root, "<<<<")
    print("current index", index)
    print("current lvl", lvl)
    """
    level = array[lvl]                          # current root's child level
    collected_list.append(root)                 # store root element
    lvl += 1                                    # one level down from child's level
    
    if lvl < final_lvl:                         # while not reaching the bottom level
        
        findChild(level[index], index, lvl)     # left child path
        collected_list.append(brk)              # insert flag for new path
        #print('---running after index', index+1, lvl)
        index = index + 1
        #print('---level-root',level)
        findChild(level[index], index, lvl)     # right child path
        
    return

#question 1
fname = input(q1)
ans1 = checkFileExist(fname)
while True:
    if ans1:
        #question 2
        try:
            ans2 = int(input(q2))
            # check if given value is large than zero
            if ans2 >= 0:
                break
            raise ValueError
        except ValueError:
            print(err2)
            exit()            
    print(err1)
    exit()


"""

Read input text file and store data to array

"""
with open(fname) as f:
    content = f.readlines()

for lines in content:
    lines.strip()
    array.append(lines.split()) #append individual digit

"""

Add an additional empty row to the end of the array to represent null result

   1    <----- root
  1 1
 1 1 1
0 0 0 0 <----- emptyRow

"""
array_len = len(array[-1])      # find the size of the last row/list in array
emptyRow = [0*(array_len + 1)]  # create a new row with size + 1
array.append(emptyRow)          # add new row to array

root = array[0][0]              #initial root
final_lvl = len(array)          #initial number of level to loop throught

"""
loop throught the triangle/array
record the possible path
"""
findChild(root, 0, 1)           # start with top element, index 0 and child level at level 1


"""
1. Arrangle the collected_list
2. Form all the possible path

example:
    collected_list = [1, 2, 3, 4, flag, 7, flag, 5, 6]
    base_list = [1,2,3,4]
    start_index = where the first flag is, 5
    update and replace the base_list from the end part with elements after flag
    hence, 2nd list will be [1, 2, 3, 7]
    3rd list will be [1, 2, 5, 6]

3. Find all the path that yields the largest sum
"""

# Set up the base_list

for i in collected_list:
    start_index += 1
    if i == brk:
        break
    base_list.append(i)

base_list_len = len(base_list)
path_all.append(base_list[:])

# Update base_list and replace childen item after flag to form a new path

for i in collected_list[start_index:]:
    
    if i == brk:
        sub_list_len = len(path_new_sub)
        sub_list_start = base_list_len - sub_list_len
        base_list[sub_list_start :] = path_new_sub
        path_all.append(base_list[:])
        path_new_sub = []
    else:
        path_new_sub.append(i)

# Find the paths yield the largest sum

for i in path_all:
    sum_val = 0
    for j in i:
        sum_val += int(j)
    if sum_val == ans2:
        path_count += 1                 # count yielding path
        if leftMost == False:
            leftMost_list = map(int, i)           # record the leftMost path
            leftMost = True

print(msg1,path_count)
print(msg2, leftMost_list)
