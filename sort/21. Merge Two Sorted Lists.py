# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:28:53 2020

@author: steve
"""


"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = answer = ListNode(0)
        
        while l1 and l2:  #if their next exist
            if l1.val <= l2.val:
                answer.next = l1
                l1 = l1.next
            else:
                answer.next = l2
                l2 = l2.next
                
            answer = answer.next
    
        if l1:  # Check whatever that is remaining
            answer.next = l1
        else:
            answer.next = l2

        return head.next