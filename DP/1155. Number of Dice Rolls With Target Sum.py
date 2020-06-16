# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 18:50:10 2020

@author: steve
"""

"""
1155. Number of Dice Rolls With Target Sum

"""


"""
DP Problem
Runtime: 304 ms, faster than 75.11% of Python3 online submissions for Number of Dice Rolls With Target Sum.
Memory Usage: 16.1 MB, less than 30.72% of Python3 online submissions for Number of Dice Rolls With Target Sum.

"""


class Solution:
    def numRollsToTarget(self, d,f,target):
        self.target = target
        self.f = f
        self.state = {}
        
        # Most basic unit: 
        def find_next_state(cur_sum,remain_dice):

            # Already checked
            if (cur_sum,remain_dice) in self.state:
                return self.state[(cur_sum,remain_dice)]
            
            #Early termination, if unreachable
            if ((self.target - cur_sum) > (self.f*remain_dice)) or ((self.target - cur_sum) < remain_dice):
                self.state[(cur_sum,remain_dice)] = 0
                return 0
            if (self.target - cur_sum) == (self.f*remain_dice) or ((self.target - cur_sum) == remain_dice):
                self.state[(cur_sum,remain_dice)] = 1
                return 1
           
            #If not checked and reachable
            self.state[(cur_sum,remain_dice)] = 0
            for i in range(1,self.f+1):
                if cur_sum + i <= self.target:
                    self.state[(cur_sum,remain_dice)] += find_next_state(cur_sum+i,remain_dice - 1)
                
            return self.state[(cur_sum,remain_dice)] 

        find_next_state(0,d)
        return self.state[(0,d)] % (10**9 + 7)

        
        
    
    
d = 0
f = 6
target = 7


# d = 2
# f = 6
# target = 7

# d = 4
# f = 10
# target = 36

d = 30
f = 30
target = 500

d = 12
f = 12
target = 100

sol = Solution()
print(sol.numRollsToTarget(d,f,target))