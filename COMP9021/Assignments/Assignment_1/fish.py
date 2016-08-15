"""
COMP9021 Assignment 1
Task 3, Fish
Created by: Fu Zheng
Created on: 14/08/2016
Version 1.0
"""
import os.path
from sys import exit

#-----------Initialise all variable below

q1 = "Which data file do you want to use?"
err1 = "Given file name doesn't exit in working directory!"
err3 = "Given file is empty."
array = []              # content of input file
min_fish = 0            # the least fish available in town
tot_dist = 0            # total transport distance in between all towns
tot_fish = 0            # total fish available in all towns before transportation
tot_site = 0            # numbers of towns
net_fish = 0            # total fish available in all towns after transportation
avg_fish = 0            # min fish available after transportation
fish_lost_rate = 1      # fish losing rate during transportation

#-----------Functions below

def checkFileExist(filename):
    """
    Return True if file exist in current working directory, else False
    """
    return os.path.isfile(filename)

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

"""

Three senarios:
1. if total distance in between towns are large than total fishes in all towns
>>> take the least fish number in towns as result, no transportation required.

2. if all town has the same amount of fish
>>> no transportation required

3. non-equal amount of fish in between towns, distance is within losting rate
>>> losting fish = sum(towns distance differences) * losting fish rate 
total_fish = sum(total fish available in all towns) - losting fish
min fish available = total_fish / total_sites

"""
tot_site = len(array)                       # total number of towns
each_town_fish = set()

if tot_site:
    # initialise variables
    min_fish = int(array[0][1])             
    pre_dist = int(array[0][0])
    
    for i in array:
        site_fish = int(i[1])               # fish available for current town
        site_dist = int(i[0])               # distance from origin point to current town
        each_town_fish.add(site_fish)       # use set to collect tuple value
        tot_dist += (site_dist - pre_dist)  # update total distance
        tot_fish += site_fish               # update total fish available
        pre_dist = site_dist                # update previous distance
        if site_fish < min_fish:            # update minimum fish number
            min_fish = site_fish
    
    if tot_fish < tot_dist or len(each_town_fish) == 1:     # cast 1 and 2 loop below:
        avg_fish = min_fish
    else:
        net_fish = tot_fish - tot_dist * fish_lost_rate     # cast 3 loop below:
        avg_fish = int(net_fish / tot_site)
    
print("The maximum quantity of fish that each town can have is {}.".format(avg_fish))
    
