# Creates 3 classes, Point, Line and Parallelogram.
# A point is determined by 2 coordinates (int or float).
# A line is determined by 2 distinct points.
# A parallelogram is determined by 4 distint lines,
# two of which having the same slope, the other two having the same slope too.
# The Parallelogram has a method, divides_into_two_parallelograms(), that determines
# where a line, provide as arguments, can split the object into two smaller parallelograms.
#
# Written by *** for COMP9021


from collections import defaultdict
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Line:
    
    def __init__(self, pt_1, pt_2):
        self.pt_1 = Point(min(pt_1.x, pt_2.x), min(pt_1.y, pt_2.y))
        self.pt_2 = Point(max(pt_1.x, pt_2.x), max(pt_1.y, pt_2.y))
        self.isValid = self._checkLine()
        self.slope = self._slope()
        self.length = self._length()
        if not self.isValid:
            print('Cannot create line')

    def _length(self):
        x = self.pt_2.x - self.pt_1.x
        y = self.pt_2.y - self.pt_1.y
        return sqrt(x*x + y*y)

    def _checkLine(self):
        if self.pt_1.x == self.pt_2.x and self.pt_1.y == self.pt_2.y:
            return False
        return True

    def _slope(self):
        x = self.pt_1.x - self.pt_2.x
        y = self.pt_1.y - self.pt_2.y
        if x == 0:
            return 1
        if y == 0:
            return 0
        return x/y
    


class Parallelogram:

    def __init__(self, l_1, l_2, l_3, l_4):
        self.line_1 = l_1
        self.line_2 = l_2
        self.line_3 = l_3
        self.line_4 = l_4
        self.paralline = 1           #check which line parallel with line 1
        self.isValid = self._checkShape()
        if not self.isValid:
            print('Cannot create parallelogram')

    def _checkShape(self):
        l1 = self.line_1
        l2 = self.line_2
        l3 = self.line_3
        l4 = self.line_4
        # check if all line exist
        if l1.isValid and l2.isValid and l3.isValid and l4.isValid:
            #check if 2 pairs of line parallel
            if l1.slope == l2.slope and l3.slope == l4.slope and l1.slope != l3.slope:
                # check if parallel lines not on same line
                tempLine = Line(l1.pt_1, l2.pt_1)
                if tempLine.isValid:
                    if tempLine.slope != l1.slope:
                        self.paralline = 2           # line 2 parallel with line 1
                        return True
                    print('ck1-2_1')
                    return False
                tempLine = Line(l1.pt_1, l2.pt_2)   #incase the first line is at the same point
                if tempLine.isValid:
                    if tempLine.slope != l1.slope:
                        self.paralline = 2           # line 2 parallel with line 1
                        return True
                    print('ck1-2_2')
                    return False
                
            if l1.slope == l3.slope and l2.slope == l4.slope and l1.slope != l2.slope:
                # check if parallel lines not on same line
                tempLine = Line(l1.pt_1, l3.pt_1)
                if tempLine.isValid:
                    if tempLine.slope != l1.slope:
                        self.paralline = 3           # line 3 parallel with line 1
                        return True
                    print('ck1-3_1')
                    return False
                tempLine = Line(l1.pt_1, l3.pt_2)   #incase the first line is at the same point
                if tempLine.isValid:
                    if tempLine.slope != l1.slope:
                        self.paralline = 3           # line 3 parallel with line 1
                        return True
                    print('ck1-3_2')
                    return False

            if l1.slope == l4.slope and l2.slope == l3.slope and l1.slope != l2.slope:
                # check if parallel lines not on same line
                tempLine = Line(l1.pt_1, l4.pt_1)
                if tempLine.isValid:
                    if tempLine.slope != l1.slope:
                        self.paralline = 4           # line 4 parallel with line 1
                        return True
                    print('ck1-4_1')
                    return False
                tempLine = Line(l1.pt_1, l4.pt_2)   #incase the first line is at the same point
                if tempLine.isValid:
                    if tempLine.slope != l1.slope:
                        self.paralline = 4           # line 4 parallel with line 1
                        return True
                    print('ck1-4_2')
                    return False
                
            print('Check Slope: \nslope1: {},slope2: {} \nslope3: {},slope4: {}'.format(l1.slope,l2.slope,l3.slope,l4.slope))
            return False
        print('invalid line exist')
        return False

    def divides_into_two_parallelograms(self, line):
        
        if self.paralline == 2:
            if line.slope == self.line_1.slope:
                
            if line.slope == self.line_3.slope:

        if self.paralline == 3:

        if self.paralline == 4:
        
    def _inBetween(self, l_1, l_2, l_3):
        x_1 = max(l_1.pt_1.x, l_2.pt_1.x)
        x_2 = min(l_1.pt_1.x, l_2.pt_1.x)
        y_1 = max(l_1.pt_1.y, l_2.pt_1.y)
        y_2 = min(l_1.pt_1.y, l_2.pt_1.y)
        if <l_1.pt_1.x
    
line = Line(Point(4, 8), Point(4, 8))
pt_11 = Point(-2, 5)
pt_12 = Point(6, 1)
pt_21 = Point(0, 6)
pt_22 = Point(-1, 0)
pt_31 = Point(2, -1)
pt_32 = Point(3, 5)
pt_41 = Point(-3, 3)
pt_42 = Point(1, 1)
line_1 = Line(pt_11, pt_12)
line_2 = Line(pt_21, pt_22)
line_3 = Line(pt_31, pt_32)
line_4 = Line(pt_41, pt_42)
line = Line(Point(4, -2), Point(6, 10))
parallelogram = Parallelogram(line_1, line_2, line_3, line_4)
