# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:09:43 2020

@author: steve
"""
"""
1446. Consecutive Characters
"""
"""
Runtime: 56 ms, faster than 50.19% of Python3 online submissions for Consecutive Characters.
Memory Usage: 13.7 MB, less than 85.33% of Python3 online submissions for Consecutive Characters.
"""

class Solution:
    def maxPower(self, s: str) -> int:
        ls = ['dummy']
        max_length = 0
        
        for let in s:
            last_let = ls[-1]
            if let == last_let:
                ls.append(let)
            else:
                if max_length < len(ls):
                    max_length = len(ls)
                ls = [let]
            # print(ls)
            
        if max_length < len(ls):
                max_length = len(ls)
                
        return max_length