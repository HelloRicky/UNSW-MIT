# Randomly generates a binary search tree with values from 0 up to 9, and displays it growing up.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, choice
from binary_tree import *
valList = list()

def print_tree_growing_down(tree):
    #printDownTree(tree, 0, tree.height())
    
    traverse(tree)
    while valList:
        item = valList.pop()
        line = ' '.join(item)
        line = line.replace('None', ' ')
        print(line)
    

# Possibly write additional function(s)
def traverse(tree):
    thislevel = [tree]
    while thislevel and len(valList) <= tree.height():
        nextlevel = list()
        val = list()
        gap = " "*(2**(tree.height() - len(valList))-1)
        for n in thislevel:
            txt = gap + str(n.value) + gap
            val.append(txt)
            if n.left_node: nextlevel.append(n.left_node)
            if n.right_node: nextlevel.append(n.right_node)
        if valList:
            parent = valList[-1]
            parentSize = len(parent)
            for i in range(parentSize):
                if 'None' in parent[i].strip():
                    val.insert(i*2, gap + 'None' + gap)
                    val.insert(i*2, gap + 'None' + gap)
        valList.append(val)
        thislevel = nextlevel

provided_input = input('Enter two integers, with the second one between 0 and 10: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    seed_arg = int(provided_input[0])
    nb_of_nodes = int(provided_input[1])
    if nb_of_nodes < 0 or nb_of_nodes > 10:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
data_pool = list(range(nb_of_nodes))
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = choice(data_pool)
    tree.insert_in_bst(datum)
    data_pool.remove(datum)
print_tree_growing_down(tree)
           
