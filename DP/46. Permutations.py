# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 21:34:35 2020

@author: steve
"""

"""
46. Permutations
https://leetcode.com/problems/permutations/

"""

    
"""
    Level0: []
    level1: [1]                  [2]              [3]
    level2: [1,2]    [1,3]       [2,1] [2,3]      [3,1] [3,2]
    level3: [1,2,3]  [1,3,2]     [2,1,3][2,3,1]   [3,1,2][3,2,1]          

"""


"""

25 / 25 test cases passed.
Status: Accepted
Runtime: 48 ms
Memory Usage: 14.3 MB
"""

class Solution:
    def permute(self, nums):
               
        self.diction = {1:[]}
        
        for number in nums:
            self.diction[1].append([number])

        
        def find_inner_level(n,nums):
            if n in self.diction:
                return self.diction[n]
            
            inner_level = find_inner_level(n-1,nums)
            self.diction[n] = []


            # This part is not very optimal, because of the O(n) many many times
            for number in nums:
                for combos in inner_level:
                    combo = combos.copy()
                    if number not in combo:
                        combo.append(number)
                        self.diction[n].append(combo)
            
            return self.diction[n]
            
        
        result = (find_inner_level(len(nums),nums))
        return result

            
            
            
        
nums = [1,2,3]
# nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.permute(nums))