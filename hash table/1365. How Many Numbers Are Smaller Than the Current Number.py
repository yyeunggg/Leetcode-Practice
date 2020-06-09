# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:38:53 2020

@author: steve
"""

"""
1365. How Many Numbers Are Smaller Than the Current Number

"""


"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""

def smallerNumbersThanCurrent(nums):
    nums_dict = {}
    nums_orig = nums.copy()
    nums.sort()     #Time complexity(nlogn)
    
    for index,num in enumerate(nums):       #O(n)
        if num not in nums_dict:
            nums_dict[num] = index
    
    ans_list = []
    for num in nums_orig:       #O(n)
        ans_list.append(nums_dict[num])     #Append O(1)
        
    return ans_list
    
    


nums = [6,5,4,8]
nums = [7,7,7,7]
smallerNumbersThanCurrent(nums)