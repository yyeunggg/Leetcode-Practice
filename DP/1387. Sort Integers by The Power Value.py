# -*- coding: utf-8 -*-
"""
Created on Fri May 29 18:50:52 2020

@author: steve
"""

"""
1387. Sort Integers by The Power Value
https://leetcode.com/problems/sort-integers-by-the-power-value/
"""

"""
DP and hashtable
"""

def getKth(lo,hi,k):
    
    powerdict = {}
    powerdict[1] = 0
    powerdict[2] = 1
    

    
    def power(n):          
        if n in powerdict:
            step = powerdict[n]
            return step
        else:
            if n%2 == 0:
                step = power(n//2) + 1
            else:
                step = power(3*n+1) + 1
            powerdict[n] = step
        return step
       
    answer_range = []    
    for number in range(lo,hi+1):
        power(number)
        answer_range.append((number,powerdict[number]))
        
    answer_sorted = sorted(answer_range,key = lambda x: x[1])
    
    
    return answer_sorted[k-1][0]
    
        
    
    
    
    
    
lo = 12
hi = 15
k = 2


# getKth(lo,hi,k)
print(getKth(lo,hi,k))