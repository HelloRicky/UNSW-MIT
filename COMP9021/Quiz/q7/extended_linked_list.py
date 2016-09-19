# Written by Fu Zheng for COMP9021

from linked_list import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)
  
    def rearrange(self):
        # initia variables
        count = 0                                   
        pre_List = LinkedList()                     # list to store nodes before mid node (included)
        aft_List = LinkedList()                     # list to store nodes after mid node

        mid_node_pos = len(self) // 2               # index of middle value

        node = self.head

        # loop to mid node
        while count < mid_node_pos:
            node = node.next_node
            count += 1

        aft_List.head = node.next_node              # store nodes after mid node
        node.next_node = None                       # split list for pre_List
        self.reverse()

        pre_List.head = self.head.next_node         # skip the head node
        pre_node = pre_List.head
        aft_node = aft_List.head

        while aft_node:
            temp_node_pre = pre_node.next_node
            temp_node_aft = aft_node.next_node
            pre_node.next_node = aft_node
            aft_node.next_node  = temp_node_pre
            pre_node = temp_node_pre
            aft_node = temp_node_aft

       