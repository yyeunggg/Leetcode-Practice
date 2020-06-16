# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:22:37 2020

@author: steve
"""

"""
1027. Longest Arithmetic Sequence


Runtime: 1344 ms, faster than 62.67% of Python3 online submissions for Longest Arithmetic Sequence.
Memory Usage: 371.7 MB, less than 18.60% of Python3 online submissions for Longest Arithmetic Sequence.

"""
class Solution:
    def longestArithSeqLength(self,A):
        
        dp = {}
        
        for i in range(len(A)):
            for j in range(i+1,len(A)):     #Only look at points after
                # print(A[i],A[j])
                number = A[j]
                difference = - A[i] + number
                # print(difference)
                dp[(j,difference)] = dp.get((i,difference),0) + 1
        
        ans = max(dp.values())+1
        print(dp)
        # print(max(dp.values())+1)
        return ans
        
        
        



A = [24,13,1,100,0,94,3,0,3]
A = [3,6,9,12]
sol = Solution()
print(sol.longestArithSeqLength(A))