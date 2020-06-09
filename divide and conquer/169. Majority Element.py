# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:30:05 2020

@author: steve
"""

"""
169. Majority Element

"""

# -- OK
def majorityElement(nums):
    #Use Moore's Voting
    
    counter = 1
    candidate = 0
    bar = len(nums)//2
    
    for number in nums:  
        if number == candidate:
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            candidate = number
            counter = 1
    return candidate
    

# Else use median --Fast
def majorityElement(nums):
    nums.sort()
    return nums[len(nums)//2]


# Brute force -- Slow
def majorityElement(nums):
    count = {}
    for number in nums:
        if number not in count:
            count[number] = 0
        count[number] += 1
    return max(count,key = count.get)

# Brute force
def majorityElement(nums):
    numbers = list(set(nums))       #Convert to [1,2]
    for num in numbers:
        count = nums.count(num)
        if count > len(nums)//2:
            return num


nums = [2,2,1,1,1,2,2]
# nums = [3,3,4]
print(majorityElement(nums))