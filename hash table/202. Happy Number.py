# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 19:24:00 2020

@author: steve
"""

"""
202. Happy Number
https://leetcode.com/problems/happy-number/
"""


def isHappy(n):
    def compute_sum(number):
        sqr_sum = 0
        while number:
            rem = number % 10
            sqr_sum += rem**2
            number  //= 10
        return sqr_sum
    
    sqr_sum = compute_sum(n)
    visited = {n}
    
    
    while sqr_sum != 1:
        sqr_sum = compute_sum(sqr_sum)
        if not (sqr_sum in visited): 
            visited.add(sqr_sum)
        else:
            return False
    
    return True
        
n = 19
print(isHappy(n))