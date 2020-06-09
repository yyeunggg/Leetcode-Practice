# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:21:03 2020

@author: steve
"""

"""
1137. N-th Tribonacci Number

"""

def tribonacci(n):
    
    F = {}
    F[0] = 0
    F[1] = 1
    F[2] = 1
    
    def trib(n):
        if n not in F:
            result = trib(n-3) + trib(n-2) + trib(n-1)
            F[n] = result
            return result
        else:
            return F[n]
    
    return trib(n)
    
    
n = 25
print(tribonacci(n))