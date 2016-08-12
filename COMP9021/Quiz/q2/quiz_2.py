# Implements coding and decoding functions for pairs of integers.
# For coding, start at point (0, 0), move to point (1, 0), and turn
# around in an anticlockwise manner.
#
# Written by *** for COMP9021


from math import sqrt
from math import atan2, pi, ceil

hcd = 180.0 #half circle degrees
shift_dgr = 45.0

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
    print('encode({},{})'.format(x, y))
    print(output)

    
def decode(n):
    pass
    # Replace pass above with your code
    

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
