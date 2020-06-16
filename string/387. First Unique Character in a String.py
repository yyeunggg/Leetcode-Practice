# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:51:18 2020

@author: steve
"""

"""
387. First Unique Character in a String

"""

# Two hashes
class Solution:
    def firstUniqChar(self, s):
        
        mem = {}
        letter = {}  
        if not s:
            return -1
        
        for i,let in enumerate(s):
            if let not in mem:
                mem[let] = i
                letter[let] = ''
            else:
                try:
                    del letter[let]
                except:
                    pass

        for key in letter.keys():
            value = mem[key]
            return value
        
        return -1
        
        
#Use counter
"""
Runtime: 96 ms, faster than 77.73% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14 MB, less than 36.59% of Python3 online submissions for First Unique Character in a String.
"""
class Solution:
  def firstUniqChar(self, s):
      import collections
      from collections import Counter as ct
      count = ct(s)
      
      for i,let in enumerate(s):
          if count[let] == 1:
              return i
      return -1



s = 'leetcode'
# s = ""
s = "aadadaad"

sol = Solution()
print(sol.firstUniqChar(s))