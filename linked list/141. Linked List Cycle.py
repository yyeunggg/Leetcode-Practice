# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:22:04 2020

@author: steve
"""

"""
141. Linked List Cycle
"""

"""
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

# Hash Table Solution
def hasCycle(head):
    ele_list = []
    while(head):
        if head not in ele_list:
            ele_list.append(head)
            head = head.next
        else:
            return True
    return False


# Two pointer/ Floyd Turtle and Hare, O(n) but a lot faster
def hasCycle(head):
    slow = head
    fast = head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True

    return False