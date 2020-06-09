# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:43:56 2020

@author: steve
"""


"""
367. Valid Perfect Square
"""

# Brute Force O(2)
# def isPerfectSquare(num):
#     if int(num**0.5) == num**0.5:
#         return True
#     else:
#         return False
    
    
# Binary Search
def isPerfectSquare(num):
    if num == 1:
        return True
    lo = 0
    hi = num/2
    mid = int((lo+hi)/2)
    
    while lo<=hi:
        if mid**2 == num:
            return True
        elif mid**2 < num:
            lo = mid + 1
        else:
            hi = mid - 1
        mid = int((lo+hi)/2)
        # print(lo,mid,hi)
    return False
    
    
    
    
    
num = 256
print(isPerfectSquare(num))