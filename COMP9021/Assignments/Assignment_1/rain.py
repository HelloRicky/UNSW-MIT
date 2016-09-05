"""
COMP9021 Assignment 1
Task 1, Rain
Created by: Fu Zheng
Created on: 11/08/2016
Version 1.0
"""
import os.path
from sys import exit

#-----------Initialise all variable below

q1 = "Which data file do you want to use?"
q2 = "How many decilitres of water do you want to poor down?"
err1 = "Given file name doesn't exit in working directory!"
err2 = "Please give me a nonnegative integer!"
err3 = "Given file is empty."
blocks = {}

#-----------Functions below

"""check if the given file name exits in the current working directory
Return True if exits, False if doesn't
"""
def checkFileExist(filename):
    return os.path.isfile(filename)

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


with open(fname) as f:
    content = f.readlines()

# check if file is empty
if len(content) == 0:
    print(err3)
    exit()

for line in content:
    line.strip()
    lines = line.split()
    for val in lines:
        try:
            val = int(val)
        except:
            continue
        if val not in blocks:
            blocks[val] = 1
        else:
            blocks[val] += 1
#get key list
blk_keys = list(blocks.keys())
blk_keys.sort()

blk_val = 0
blk_i = 0
prev_vol = 0

while True:
    
    blk_key = blk_keys[blk_i]
    blk_val += blocks[blk_key]
    if blk_i < len(blk_keys) - 1:
        high_diff = blk_keys[blk_i + 1] - blk_key
        max_vol = high_diff * blk_val + prev_vol
        if ans2 > max_vol:
            prev_vol = max_vol
            blk_i += 1
            continue
    #else
    left_vol = ans2 - prev_vol
    final_hight = (left_vol/ blk_val) + blk_key
    break
print("The water rises to {:.2f} centimetres.".format(final_hight))
