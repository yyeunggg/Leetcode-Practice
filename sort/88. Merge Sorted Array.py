# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 19:45:07 2020

@author: steve
"""

"""
88. Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/
"""


def merge(nums1,m,nums2, n):
    answer = []
     
    i = 0
    j = 0
     
    while ((i<m) or (j<n)) and (i+j<len(nums1)):
        if nums1[i] == 0 or nums1[i] > nums2[j]:
            answer += [nums2[j]]
            j += 1
        else:
            answer += [nums1[i]]
            i += 1
    
    return answer
    
# However, we have to change nums1, so we have to utilize the list backward
def merge(nums1,m,nums2, n):
    i = m - 1
    j = n - 1
    nums1_index = len(nums1) - 1

    
    #Now we append the larger value, this is up til nums1 is completely appended
    while (i!= -1) and (j != -1) and (nums1_index!=-1):
        if nums1[i] >= nums2[j]:
            nums1[nums1_index] = nums1[i]
            i -= 1
        else:
            nums1[nums1_index] = nums2[j]
            j -= 1
        nums1_index -= 1

    #When there are remaining index
    while (nums1_index!=-1):
        if i == -1:
            nums1[nums1_index] =  nums2[nums1_index]
        else:
            nums1[nums1_index] =  nums1[nums1_index]
        nums1_index -= 1
    return nums1
        
    
    
    

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3


# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1


# nums1 = [2,0]
# m = 1
# nums2 = [1]
# n = 1

print(merge(nums1,m,nums2,n))