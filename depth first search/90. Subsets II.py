# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:13:52 2020

@author: steve
"""

"""
90. Subsets II

"""


# let's try to do it with dynamic programming

class Solution:
    def subsetsWithDup(self,nums):
        nums = sorted(nums)     #O(nlgn)
        current_layer = []
        
        self.nums = nums
        self.ans = []
        
        
        # For every layer, I want the one that pops up for the first time:
        def find_layer_path(start_index,current_layer):
            self.ans += [current_layer]     #Append successful layer
            # print(self.ans)
            
            for index in range(start_index,len(self.nums)):    # For the remaining numbers
                # I don't want to attach if it is the second time it shows up in this layer
                # It only needs to satisfy that it is num[i] != num[i-1] or it is the first one
                if (index == start_index) or self.nums[index-1] != self.nums[index]:
                    find_layer_path(index+1,current_layer+[self.nums[index]])  #We will go deeper by another layer
                    
        
        find_layer_path(0,current_layer)
        return self.ans
        
    
    
"""
structure:
        /                                           /                   \           \
        1                                        2                   2(x)          3
        /\                                      /\                  /\          /\
    [1,2] [1,2](xxxx) [1,3]                 [2,2] [2,3]

"""



nums = [1,2,2]
nums = [1,2,3,4,5,6,7,8,10,0]
sol = Solution()
print(sol.subsetsWithDup(nums))