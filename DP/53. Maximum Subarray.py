# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:59:51 2020

@author: steve
"""

"""
53. Maximum Subarray


"""

# def maxSubArray(nums):
 
#     # So we want to compute the maximum 'reward' that can be obtained by adding nums[i]
#     # Start from right to left

#     reward = [0]*len(nums)
#     reward[-1] = nums[-1]
#     max_reward = nums[-1]
     
#     for index in range(len(nums)-1)[::-1]:
#         reward[index] = max(reward[index+1] + nums[index],nums[index])
#         max_reward = max(max_reward,reward[index])
    
#     return max_reward



# Try shrinking space
def maxSubArray(nums):
 
    # So we want to compute the maximum 'reward' that can be obtained by adding nums[i]
    # Start from right to left

    max_reward = nums[-1]
    last_reward = nums[-1] 
    
    for index in range(len(nums)-1)[::-1]:
        last_reward = max(nums[index],nums[index]+last_reward)
        max_reward = max(max_reward, last_reward)
        
    return max_reward


a = [-2,1,-3,4,-1,2,1,-5,4]
# a = [1]
print(maxSubArray(a))
