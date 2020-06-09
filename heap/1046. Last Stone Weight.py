# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:13:07 2020

@author: steve
"""

"""
1046. Last Stone Weight
"""


# Brute Force Solving (O(nlgn))
def lastStoneWeight(stones):
    stones.sort()
    stones_remain = stones.copy()
    while len(stones_remain)!= 1:
        w_diff = stones_remain[-1] - stones_remain[-2]
        stones_remain.pop(-1)
        stones_remain.pop(-1)
        stones_remain = stones_remain + [w_diff]
        stones_remain.sort()
    return stones_remain[0]
    
stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones))