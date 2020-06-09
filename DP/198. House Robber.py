# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:58:35 2020

@author: steve
"""

"""
198. House Robber
"""

# Dynamic Programming, pretty straightforward
def rob(nums):
    if nums == []:
        return 0
    
    mem = [None]*len(nums)
    
    
    def steal(n):
        if mem[n]!= None:
            result = mem[n]
        elif n == 0:
            result = nums[0]
        elif n == 1:
            result = max(nums[1],nums[0])
        else:
            result = max(nums[n]+steal(n-2), steal(n-1))
        mem[n] = result
        print(mem)
        return result
    

    return steal(len(nums)-1)
        
        
    




nums = [1,2,3,1,11,23,231,21,21,32,31,41,4,1,51,2]

rob(nums)