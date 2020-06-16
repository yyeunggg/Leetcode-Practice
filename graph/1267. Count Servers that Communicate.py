# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 17:29:21 2020

@author: steve
"""



"""
1267. Count Servers that Communicate
https://leetcode.com/problems/count-servers-that-communicate/
"""

"""
Runtime: 508 ms, faster than 75.04% of Python3 online submissions for Count Servers that Communicate.
Memory Usage: 15.1 MB, less than 82.93% of Python3 online submissions for Count Servers that Communicate.
Next challenges:
"""

class Solution:
    def countServers(self, grid):
        
        import collections
        # Create a set
        rows = collections.defaultdict(int)
        cols = collections.defaultdict(int)
        
        # Initiate answer
        ans = 0
        
        # Count
        for i,row in enumerate(grid):
            for j, comp in enumerate(row):
                if comp:
                    rows[i] += 1
                    cols[j] += 1
        
        
        for i,row in enumerate(grid):
            for j, comp in enumerate(row):
                if comp:
                    if rows[i] > 1 or cols[j] > 1:
                        ans += 1

        return ans

    

grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
grid = [[1,0],[1,1]]

sol = Solution()
print(sol.countServers(grid))