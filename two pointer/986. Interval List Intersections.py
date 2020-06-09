# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:53:13 2020

@author: steve
"""

"""

986. Interval List Intersections

"""


def intervalIntersection(A,B):

    # Use two pointers
    a_i = 0
    b_i = 0
    
    # Initiate answer
    ans = []
    
    while a_i < len(A) and b_i < len(B):
        a_start, a_end = A[a_i]
        b_start, b_end = B[b_i]
        
        # a_start < b_end and b_start < a_end  -->  means that there is an overlap
        if a_start <= b_end and b_start <= a_end:
            start = max(a_start,b_start)
            end = min(a_end,b_end)
            ans.append([start,end])
            
            # Update pointer, if the range is already covered
            if end >= a_end: 
                a_i += 1               
            if end >= b_end:
                b_i += 1
            
        # move pointer for the smaller one if there is no overlap
        elif a_end <= b_start:
            a_i += 1
        else:
            b_i += 1
            
    return ans
    
    
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

# A = [[14,16]]
# B = [[7,13],[16,20]]


print(intervalIntersection(A,B))