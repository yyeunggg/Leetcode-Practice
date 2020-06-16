# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:26:37 2020

@author: steve
"""

"""

26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


"""
Runtime: 88 ms, faster than 60.77% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.5 MB, less than 72.65% of Python3 online submissions for Remove Duplicates from Sorted Array.

"""


class Solution:
    def removeDuplicates(self, nums):
        length = 0
        for i, number in enumerate(nums[:-1]):
            if number != nums[i+1]:
                length += 1
                nums[length] = nums[i+1]    #Swap this element with the next unique number
                
        return length+1
                
        
        
        
        
    
    
    
nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))
        