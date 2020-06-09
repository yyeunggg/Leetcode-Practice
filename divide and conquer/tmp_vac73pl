# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 14:42:59 2020

@author: steve
"""

"""

215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

def findKthLargest(nums,k):
    import heapq
    
    inv_nums = []
    for x in nums:  #O(n)
        inv_nums.append(-x)
        
    heapq.heapify(inv_nums) #O(n)
        
    i = 0
    while i < k-1: #O(k)
        heapq.heappop(inv_nums)
        i += 1
        
    return -heapq.heappop(inv_nums)


# O(nlgn) sort
def findKthLargest(nums,k):
    nums = sorted(nums,reverse = True)
    print(nums)
    return (nums[k-1])

nums = [3,2,1,5,6,4]
k = 2


# nums = [3,2,3,1,2,4,5,5,6]
# k = 4

print(findKthLargest(nums,k))