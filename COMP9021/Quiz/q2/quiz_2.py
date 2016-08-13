# Implements coding and decoding functions for pairs of integers.
# For coding, start at point (0, 0), move to point (1, 0), and turn
# around in an anticlockwise manner.
#
# Written by FU ZHENG for COMP9021


from math import sqrt
from math import atan2, pi, ceil

hcd = 180.0 #half circle degrees
shift_dgr = 45.0

""" 
find max num in the loop x
e.g. x = 1, maxnum = 8
x = 3, maxnum = 48

"""
def maxLoopNum(x):
    val = 0
    
    if x > 0:
        corner = 4
        face = 4
        
        for i in range(1, x + 1):
            gap = 2*i - 1
            val += gap * face + corner
        return val
    return val

"""
get the coordination with the:
orient_count: sector number, from 1 - 8
lp_num: the magnitute of the point
mov: the diff val from current sector to previous sector

5 . 4 . 3
. . . . .
6 . 0 . 2
. . . . .
7 . 8 . 1

""" 
def getCoordination(orient_count, lp_num, mov):
    if orient_count <= 2:
        x = lp_num
        if orient_count == 1:
            y = -mov
        else:
            y = lp_num - mov
        #print('x:',x, 'y:',y)
        return x, y
    if orient_count <= 4:
        y = lp_num
        if orient_count == 3:
            x = mov
        else:
            x = -lp_num + mov

        #print('x:',x, 'y:',y)
        return x, y
    if orient_count <= 6:
        x = - lp_num
        if orient_count == 5:
            y = mov
        else:
            y = -lp_num + mov
        
        #print('x:',x, 'y:',y)
        return x, y
    if orient_count <= 8:
        y = - lp_num
        if orient_count == 7:
            x = -mov
        else:
            x = lp_num - mov
        #print('x:',x, 'y:',y)
        return x, y
"""
use the percentage of the bearing to find the position of n in 360 degress
"""

def encode(x, y):
    loop_num = max(abs(x),abs(y))
    if y == 0 and x >= 0:
        bearing = 0
    else:
        bearing = hcd / (pi/atan2(y,x))
        
    bearing += shift_dgr

    if bearing < 0:
        bearing = 2*hcd + bearing
        
    #print('bearing is',bearing)
    temp = 2*hcd
    percent_bearing = bearing / (2*hcd)
    #print('percentage of bearing', percent_bearing)

    startNum = maxLoopNum(loop_num -1)

    endNum = maxLoopNum(loop_num)
    gapNum = endNum - startNum
    if bearing == 0:
        output = endNum
    else:
        output = int(round(gapNum*percent_bearing+startNum))

    """
    print('startNum',startNum)
    print('endNum',endNum)
    print('diff',gapNum)
    print('bearing', bearing,'percentage>',percent_bearing)
    """
    #print('encode({},{})'.format(x, y))
    return output

"""
1. find the loop level of the input n
2. find the diff from max to n
3. find the located sectors (8 sectors represents 8 orientations)
"""
def decode(n):
    max_num = 0
    lp_num = 0
    gap_point = 8
    orient_count = 0
    x = 0
    y = 0
    #print('input n:',n)
    
    while n > max_num:
        lp_num += 1
        max_num = maxLoopNum(lp_num)
        
    min_num = maxLoopNum(lp_num - 1) + 1
    prev_point = min_num
    #print('loop number',lp_num)
    #print('min number',min_num)
    #print('max number',max_num)
    de_gap = max_num - min_num + 1
    gap_interval = (de_gap - gap_point)/gap_point
    #print('gap_interval', gap_interval)
    for i in range(gap_point+1):
        orient_count += 1
        point_val = min_num + (i*(gap_interval+1)) - 1
        if point_val >= n:
            #print('within', prev_point, point_val)
            
            mov = point_val - n
            orient_count -= 1
            #print('orient',orient_count)
            #print('mov',mov)
            x, y = getCoordination(orient_count, lp_num, mov)
            
            #print('decode({})'.format(n))
            print('({:}, {:})'.format(int(x),int(y)))
            break
        prev_point = point_val

"""
test example

encode(0, 0)
encode(1, 0)
encode(1, 1)
encode(0, 1)
encode(-1, 1)
encode(-1, 0)
encode(-1, -1)
encode(0, -1)
encode(1, -1)
encode(2, -1)
encode(2, 0)
encode(2, 1)
encode(2, 2)
encode(1, 2)
encode(0, 2)
encode(4, -2)


decode(0)
decode(1)
decode(2)
decode(3)
decode(4)
decode(5)
decode(6)
decode(7)
decode(8)
decode(9)
decode(10)
decode(11)
decode(12)
decode(13)
decode(14)
decode(50)
"""
