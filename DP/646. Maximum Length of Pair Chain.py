# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:09:21 2020

@author: steve
"""

"""
646. Maximum Length of Pair Chain

https://leetcode.com/problems/maximum-length-of-pair-chain/
"""
# Can use DP in this problem
"""
Runtime: 2240 ms, faster than 39.90% of Python3 online submissions for Maximum Length of Pair Chain.
Memory Usage: 14.3 MB, less than 49.78% of Python3 online submissions for Maximum Length of Pair Chain.
"""
class Solution:    
    def findLongestChain(self, pairs):
        pairs = sorted(pairs)   #O(nlgn)
        indices = {}
        global_max = 0

        
        for pair in pairs:
            if pair[1] not in indices:
                indices[pair[1]] = 1
            for end_points in indices:
                if end_points < pair[0]:
                    indices[pair[1]] = max(indices[pair[1]],indices[end_points]+1)
            global_max = max(global_max,indices[pair[1]])
            
        return global_max
            


"""
Much much faster
Runtime: 208 ms, faster than 95.84% of Python3 online submissions for Maximum Length of Pair Chain.
Memory Usage: 14 MB, less than 89.38% of Python3 online submissions for Maximum Length of Pair Chain.
"""
    
class Solution:    
    def findLongestChain(self, pairs):
        pairs = sorted(pairs,key = lambda x: x[1])   #O(nlgn,sort based on end point, so that long intervals will be thrown to back)
        global_max = 0       
        current_point = [-float('inf'),-float('inf')]
        
        for pair in pairs:
            if pair[0] > current_point[1]:
                current_point = pair
                global_max += 1
            
        return global_max
            
        
        
pairs = [[1,2], [2,3], [3,4]]
pairs = [[1,2], [2,3], [3,4],[4,5],[6,7],[7,8],[7,9],[6,7],[4,7],[1,3]]
sol = Solution()
print(sol.findLongestChain(pairs))