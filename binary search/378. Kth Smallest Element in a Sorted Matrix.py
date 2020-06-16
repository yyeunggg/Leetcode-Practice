# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:47:22 2020

@author: steve
"""

"""
378. Kth Smallest Element in a Sorted Matrix


"""
"""
Runtime: 260 ms, faster than 25.97% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 19.8 MB, less than 30.20% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
"""
class Solution:
    def kthSmallest(self, matrix, k):
        #Using basic heap
        import heapq
        mat_to_list = []
        for rows in matrix:
            mat_to_list += rows
            
        heapq.heapify(mat_to_list)
        
        i = 0
        while i < k-1:
            heapq.heappop(mat_to_list)
            i += 1
            
        return heapq.heappop(mat_to_list)
        
        
        
"""
Check if there is an alternative
Runtime: 168 ms, faster than 96.67% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 19.8 MB, less than 27.89% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
"""
# Basic sort
class Solution:
    def kthSmallest(self, matrix, k):
        mat_to_list = []
        for rows in matrix:
            mat_to_list += rows
            
        return sorted(mat_to_list)[k-1]
        

"""
Let's try binary search

"""
class Solution:
    def kthSmallest(self, matrix, k):
        
        
        
        
matrix = [[ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
k = 4
sol = Solution()
print(sol.kthSmallest(matrix,k))