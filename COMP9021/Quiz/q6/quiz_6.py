# Creates 3 classes, Point, Line and Parallelogram.
# A point is determined by 2 coordinates (int or float).
# A line is determined by 2 distinct points.
# A parallelogram is determined by 4 distint lines,
# two of which having the same slope, the other two having the same slope too.
# The Parallelogram has a method, divides_into_two_parallelograms(), that determines
# where a line, provide as arguments, can split the object into two smaller parallelograms.
#
# Written by FU ZHENG for COMP9021


from collections import defaultdict
from math import sqrt
from math import inf


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Line:
    
    def __init__(self, pt_1, pt_2):
        self.pt_1 = pt_1
        self.pt_2 = pt_2
        self.isValid = self._checkLine()
        self.slope = self._slope()
        self.length = self._length()
        self.intersect_x = self._intersect_x()
        self.intersect_y = self._intersect_y()
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
            return inf
        if y == 0:
            return 0
        return y/x

    def _intersect_x(self):
        if self.slope == inf:
            return self.pt_1.x
        if self.slope == 0:
            return None
        return -self.pt_1.y/self.slope + self.pt_1.x

    def _intersect_y(self):
        if self.slope == inf:
            return None
        if self.slope == 0:
            return self.pt_1.y
        return self.pt_1.y - self.pt_1.x * self.slope


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
                if not (l1.intersect_x == l2.intersect_x and l1.intersect_y ==l2.intersect_y):
                    self.paralline = 2           # line 2 parallel with line 1
                    return True
                return False
                
            if l1.slope == l3.slope and l2.slope == l4.slope and l1.slope != l2.slope:
                # check if parallel lines not on same line
                if not (l1.intersect_x == l3.intersect_x and l1.intersect_y ==l3.intersect_y):
                    self.paralline = 3           # line 3 parallel with line 1
                    return True
                return False

            if l1.slope == l4.slope and l2.slope == l3.slope and l1.slope != l2.slope:
                # check if parallel lines not on same line
                if not (l1.intersect_x == l4.intersect_x and l1.intersect_y ==l4.intersect_y):
                    self.paralline = 4           # line 4 parallel with line 1
                    return True
                return False
                
            #print('Check Slope: \nslope1: {},slope2: {} \nslope3: {},slope4: {}'.format(l1.slope,l2.slope,l3.slope,l4.slope))
            return False
        #print('invalid line exist')
        return False

    def divides_into_two_parallelograms(self, line):
        
        if self.paralline == 2:
            
            if line.slope == self.line_1.slope:
                #print('1-2_1')
                return self._inBetween(self.line_1, self.line_2, line)
            if line.slope == self.line_4.slope:
                #print('1-2_2')
                return self._inBetween(self.line_4, self.line_3, line)
            
        if self.paralline == 3:
            if line.slope == self.line_1.slope:
                #print('1-3_1')
                return self._inBetween(self.line_1, self.line_3, line)
            if line.slope == self.line_4.slope:
                #print('1-3_2')
                return self._inBetween(self.line_4, self.line_2, line)
            
        if self.paralline == 4:
            if line.slope == self.line_1.slope:
                #print('1-4_1')
                return self._inBetween(self.line_1, self.line_4, line)
            if line.slope == self.line_2.slope:
                #print('1-4_2')
                return self._inBetween(self.line_2, self.line_3, line)
        return False
    
    def _inBetween(self, l_1, l_2, l_3):
        if l_1.slope == inf:
            x_1 = min(l_1.intersect_x, l_2.intersect_x)
            x_2 = max(l_1.intersect_x, l_2.intersect_x)
            #print('b1',x_1 < l_3.intersect_x < x_2)
            return x_1 < l_3.intersect_x < x_2
        y_1 = min(l_1.intersect_y, l_2.intersect_y)
        y_2 = max(l_1.intersect_y, l_2.intersect_y)
        #print('b2',y_1 < l_3.intersect_y < y_2)
        return y_1 < l_3.intersect_y < y_2

"""
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
parallelogram = Parallelogram(line, line_2, line_3, line_4)
parallelogram = Parallelogram(line_1, line_2, line_3, line_1)

line = Line(pt_41, Point(1, 2))
parallelogram = Parallelogram(line_1, line_2, line_3, line)

parallelogram = Parallelogram(line_1, line_2, line_3, line_4)

pt_1 = Point(-1, 4)
pt_2 = Point(2, 2)
line = Line(pt_1, pt_2)
parallelogram.divides_into_two_parallelograms(line)

pt_1 = Point(-2, 4)
line = Line(pt_1, pt_2)
parallelogram.divides_into_two_parallelograms(line)

parallelogram.divides_into_two_parallelograms(line_2)

line = Line(Point(0, -2), Point(0, 7))
parallelogram.divides_into_two_parallelograms(line)

line = Line(Point(-1, -3), Point(2, 15))
parallelogram.divides_into_two_parallelograms(line)
"""
