# -*- coding: utf-8 -*-
"""
Created on Fri May 29 17:42:13 2020

@author: steve
"""


"""
1338. Reduce Array Size to The Half

"""

def minSetSize(arr):
    import collections
    from collections import Counter as ct
    count = ct(arr).most_common()
    
    n = 0
    n_count = 0

    
    for number in count:       
        n += number[1] 
        n_count += 1
        
        if n >= len(arr)//2:
            return n_count
    
    
    
    
arr = [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]
print(minSetSize(arr))