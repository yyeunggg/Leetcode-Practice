# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:07:24 2019

@author: stevie
"""

"""First iteration
def findMedianSortedArrays(nums1,nums2) -> float:
    num3 = nums1+nums2
    num3.sort()
    length = len(num3)
    if length % 2 !=0:
        med = num3[int((length)/2)]
    else:
        med = (num3[int((length-1)/2)]+num3[int((length+1)/2)])/2
    return med
"""#Result is 44ms, faster than 91.22%

#Using Binary Search


def findMedianSortedArrays(nums1,nums2) -> float:
    #find the length of two lists
    len1 = len(nums1)
    len2 = len(nums2)
    
    #Ensure len2 > len1
    if len1 > len2:
        len1, len2, nums1, nums2 = len2, len1, nums2, nums1
    
    #Emsure at least one list is not empty
    if len2 == 0:
        print('NOOO')
        
    #Initialize Binary Search
    #Range of search [imin,imax]
    imin, imax = 0, len1
    i_mid = int((len1+len2+1)/2)
    
    #Starting the loop:
    while imin <= imax:  #Make sure don't move all the way
        if len1+len2 == 1:
            return nums2[0]
        i = int((imin+imax)/2) #Index i to look at (for list 1)
        j = i_mid - i   #Index j to look at (for list 2)
 #       print('i:',i,'///A,B:',nums1[i-1],nums1[i],nums2[j-1],nums2[j])
        if i < len1 and nums2[j-1] > nums1[i]:  #i is too small, needs to move right for first list
                #In case i = len1-1, it means that list 1 is completely smaller than list 2
            imin = i+1
        elif i>0 and nums1[i-1]>nums2[j]:
                #In case i = 1, j = len1, it means that list 1 is completely greater than list 2
            imax = i-1
        else:
            if i == 0:
                max_left = nums2[j-1]
            elif j == 0:
                max_left = nums1[i-1]
            else:
                max_left = max(nums1[i-1],nums2[j-1])
                
                ##If list1+list2 has an odd number of entry
            if (len1+len2)%2 == 1:
                return max_left
            
            if i == len1: 
                print(i,j)
                min_right = nums2[j]
            elif j == len2:
                min_right = nums1[i]
            else:
                min_right= min(nums1[i],nums2[j])
            return (max_left+min_right)/2
        


nums1 = [3]
nums2 = [-2,-1]
med =  findMedianSortedArrays(nums1,nums2)
a = nums1+nums2
a.sort()
print(a, 'median is', med)