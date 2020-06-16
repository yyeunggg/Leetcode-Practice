# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:50:48 2020

@author: steve
"""

"""

120. Triangle

https://leetcode.com/problems/triangle/
"""
"""
Runtime: 104 ms, faster than 6.93% of Python3 online submissions for Triangle.
Memory Usage: 15.1 MB, less than 10.52% of Python3 online submissions for Triangle.

"""
class Solution:
    def minimumTotal(self, triangle):
        
        self.triangle = triangle
        self.depth = len(triangle)
        self.dp = [[None for x in range(self.depth)] for x in range(self.depth)]       
        self.dp[-1] = triangle[-1].copy()   #Want to go from the deepest, as N

        
        def find_cost(layer_depth, position):
            if self.dp[layer_depth][position] != None:
                return self.dp[layer_depth][position]       
            for i, selfcost in enumerate(self.triangle[layer_depth]):
                cost_left = find_cost(layer_depth+1, i)
                cost_right = find_cost(layer_depth+1, i+1)
                total_opt_cost = selfcost + min(cost_left,cost_right)
                self.dp[layer_depth][i] = total_opt_cost       
            return self.dp[layer_depth][position]

        find_cost(0,0)
        return self.dp[0][0]



"""
Runtime: 72 ms, faster than 23.89% of Python3 online submissions for Triangle.
Memory Usage: 14.6 MB, less than 53.23% of Python3 online submissions for Triangle.
"""
class Solution:
    def minimumTotal(self, triangle):
        
        # TBH, we only need to add each layer, for this one, it is faster than DP
        
        for row in range(len(triangle)-1)[::-1]:
            for i in range(len(triangle[row])):
                triangle[row][i] += min(triangle[row+1][i],triangle[row+1][i+1])

        return triangle[0][0]
        
           
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[2],[3,4],[6,5,9],[4,4,8,0]]
sol = Solution()
print(sol.minimumTotal(triangle))