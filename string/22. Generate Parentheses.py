# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:02:22 2020

@author: steve
"""

"""

22. Generate Parentheses

"""

"""
Runtime: 44 ms, faster than 22.90% of Python3 online submissions for Generate Parentheses.
Memory Usage: 14 MB, less than 60.77% of Python3 online submissions for Generate Parentheses.
"""

class Solution:
    
    def generateParenthesis(self, n):


        # self.mem = {1:("()")}
        self.mem = {}
        self.mem[1] = ['()']
        # print(self.mem)
        
        def find_shallow(n):
            if n in self.mem:
                return self.mem[n]
            
            current_layer = set()
            shallow_layer = find_shallow(n-1)
            # print(shallow_layer)
            
            for element in shallow_layer:
                # print(element)
                # print("(" + element + ")")
                for i in range(len(element)):
                    current_layer.add(element[:i] + '()' + element[i:])     #The rule of adding ()
                    # current_layer.add('()' + element)
                    # current_layer.add(element+'()')
            
            # print(current_layer)
            self.mem[n] = current_layer
            # print(self.mem)
                    
            return list(current_layer)
        
        ans = find_shallow(n)
        return ans
            
            
            
        
        
        
        
        
    
n = 4
sol = Solution()
ans1 = sol.generateParenthesis(n)
print(ans1)

ans = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
# print(ans)


