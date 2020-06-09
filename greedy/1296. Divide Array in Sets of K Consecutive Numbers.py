# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:52:33 2020

@author: steve
"""

"""
1296. Divide Array in Sets of K Consecutive Numbers
https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""

# I think the easiest way for me is to sort it first


"""
Runtime: 6788 ms, faster than 5.02% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
Memory Usage: 25.8 MB, less than 96.45% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
"""
def isPossibleDivide(nums,k):
    if len(nums) % k != 0:
        return False
   
    nums = sorted(nums) #Requires O(nlogn)
    
    while nums: #(K*n)
        check_num = nums[0]
        for i in range(check_num,check_num + k):
            try:
                nums.remove(i)
            except:
                return False
        
    return True
    


"""
Alright, let's do hands of straight style
Runtime: 448 ms, faster than 79.20% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
Memory Usage: 28.5 MB, less than 77.21% of Python3 online submissions for Divide Array in Sets of K Consecutive Numbers.
"""
def isPossibleDivide(nums,k):
    import collections
    from collections import Counter as ct
    count = ct(nums)

    
    number_list = sorted(count)
    
    for numbers in number_list:
        if count[numbers] >= 1:
            for i in range(numbers,numbers + k)[::-1]:  #Here use backward
                count[i] -= count[numbers]
                if count[i] < 0:
                    return False
                
    return True
        
        



nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k = 3
print(isPossibleDivide(nums,k))