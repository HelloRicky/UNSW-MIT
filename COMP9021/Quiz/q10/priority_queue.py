# Code for insertion into a priority queue
# implemented as a binary tree
#
# Written by *** for COMP9021


from binary_tree import *
from math import log


class PriorityQueue(BinaryTree):
    def __init__(self):
        super().__init__()

    def insert(self, value):
        if self.value is None:
            self._insert(value)
        elif self.right_node.value is None:
            self._insert(value)
            self.sortTree()
        else:
            if self.left_node.right_node.value is None:
                self.left_node._insert(value)
                self.sortTree()
                self.sortall()
            elif self.right_node.right_node.value is None:
                self.right_node._insert(value)
                self.sortTree()
                self.sortall()
            else:
                old=self
                self=self.left_node          
                if self.left_node.right_node.value is None:
                    self.left_node._insert(value)
                    self.sortTree()
                    old.sortall()
                elif self.right_node.right_node.value is None:
                    self.right_node._insert(value)
                    self.sortTree()
                    old.sortall()
    def _insert(self,value):
        if self.value is None:
            self.value = value
            self.left_node = PriorityQueue()
            self.right_node = PriorityQueue()
        else:
            if self.left_node.value is None:
                self.left_node._insert(value)
            else:
                self.right_node._insert(value)
                
    def sortTree(self):           
        if self.left_node.value is not None:
            if self.left_node.left_node.value is not None or self.left_node.right_node.value is not None:
                self.left_node.sortTree()
            else:
                if self.left_node.value<self.value:
                    a=self.value
                    self.value=self.left_node.value
                    self.left_node.value=a
        if self.right_node.value is not None:
            if self.right_node.left_node.value is not None or self.right_node.right_node.value is not None:
                self.right_node.sortTree()
            else:
                 if self.right_node.value<self.value:
                     a=self.value
                     self.value=self.right_node.value
                     self.right_node.value=a
    def sortall(self):
        self.left_node.repeatsort()
        self.right_node.repeatsort()
        self.repeatsort()
        
    def repeatsort(self):
        if self.left_node.value is not None and self.left_node.value<self.value:
            a=self.value
            self.value=self.left_node.value
            self.left_node.value=a
        if self.right_node.value is not None and self.right_node.value<self.value:
            a=self.value
            self.value=self.right_node.value
            self.right_node.value=a
