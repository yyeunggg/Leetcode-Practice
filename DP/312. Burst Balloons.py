# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:06:12 2020

@author: steve
"""

"""
312. Burst Balloons
https://leetcode.com/problems/burst-balloons/

"""

# Exceeds time limit
class Solutions:
    def maxCoins(self,nums):
        nums = [i for i in nums if i!=0]
        # Empty list
        if not nums:
            return 0
        self.memory = {}
        self.max_val = 0
        def find_max(self,nums):
            nums_tup = tuple(nums)
            if nums_tup in self.memory:
                return self.memory[nums_tup]         
            if len(nums) == 1:
                value = nums[0]
                self.memory[nums_tup] = value
                return value
            max_val = 0                      
            for i,number in enumerate(nums):                
                nums_list = nums[:i].copy() + nums[i+1:].copy()
                value = 0
                value = find_max(self,nums_list)                
                if i == 0:
                    value += number*nums[i+1]
                elif i != len(nums)-1:
                    value += nums[i-1]*number*nums[i+1]
                else:
                    value += number*nums[i-1]                
                if value > max_val:
                    max_val = value                
            self.memory[nums_tup] = max_val
            return max_val    
        answer = find_max(self,nums)
        return answer
    


## From leetcode discussion. This is essentially a length varying sliding window.
"""
Runtime: 528 ms, faster than 52.61% of Python3 online submissions for Burst Balloons.
Memory Usage: 14.1 MB, less than 59.48% of Python3 online submissions for Burst Balloons.
"""
class Solutions:
    def maxCoins(self,nums):
        nums = [1] + nums + [1] #Pad the list
        n = len(nums)
        dp = [[0] * n for _ in range(n)] #Store value
        
        # Start iteration
        for window_length in range(1,len(nums)+1):    #Iterate through the length of sliding window. From 1 element to n
            for start in range(0+1,len(nums)-2-window_length+1+1):  #Iterate through the starting index of window,+1 because of padding, -2 same reason
                end = start + window_length - 1
                for last_num in range(start,end+1): #Iterate through which balloon is the last one to pop, within the window
                    val = dp[start][last_num-1] + dp[last_num+1][end] + nums[last_num]*nums[start-1]*nums[end+1]
                    # Normally I would do dictionary, but using a 2-D list is the same
                    dp[start][end] = max(dp[start][end],val)

        answer = dp[1][len(nums)-2]
        return answer
    
    
nums = [9,76,64,21,97]
nums = [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2]
nums = [8,3,4,3,5,0,5,6,6,2,8,5,6,2,3,8,3,5,1,0,2,9]
sol = Solutions()
print(sol.maxCoins(nums))