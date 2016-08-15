"""
COMP9021 Assignment 1
Task 4, nonredundant
Created by: Fu Zheng
Created on: 15/08/2016
Version 1.0
"""
import os.path
from sys import exit

#-----------Initialise all variable below

q1 = "Which data file do you want to use?"
err1 = "Given file name doesn't exit in working directory!"
err3 = "Given file is empty."
msg1 = "The nonredundant facts are:"
array = []              # content of input file
routes = {}             # collect all the possible val of each key
ori_set = set()         # inital pair set
chg_set = set()         # possible Relation generated from one to another

#-----------Functions below

def checkFileExist(filename):
    """
    Return True if file exist in current working directory, else False
    """
    return os.path.isfile(filename)

def getAB(item):
    """
    Return the key and value of each R pair, int type
    """
    pair_num = item[0].split(',')
    a = int(pair_num[0].replace('R(',''))
    b = int(pair_num[1].replace(')',''))  
    return a, b

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
    array.append(lines.split()) #append individual digit

# store each pair to an dictionary, routes
for i in array:
    a, b = getAB(i)
    routes.setdefault(a,[])
    routes[a].append(b)
    
for k, v in routes.items():
    #loop for each key values
    for i in v:        
        seek_key = i
        while seek_key in routes:
            # recorded each possible route from value to key
            change_val = 'R({},{})'.format(k,routes[seek_key][0])
            chg_set.add(change_val)
            seek_key = routes[seek_key][0]  #update value as key

        # reformat data
        origin_val = 'R({},{})'.format(k,i)        
        ori_set.add(origin_val)

# exclude all duplicated set from original set
final_set = ori_set - chg_set 

print(msg1)

for i in array:
    if i[0] in final_set:
        print(i[0])
