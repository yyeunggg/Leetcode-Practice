# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:10:41 2020

@author: steve
"""

"""
1381. Design a Stack With Increment Operation

https://leetcode.com/problems/design-a-stack-with-increment-operation/
"""

"""
Runtime: 128 ms, faster than 75.86% of Python3 online submissions for Design a Stack With Increment Operation.
Memory Usage: 14.6 MB, less than 37.28% of Python3 online submissions for Design a Stack With Increment Operation.
"""

class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.stack = []
        

    def push(self, x: int) -> None:
        
        if len(self.stack) < self.max:
            self.stack.append(x)
            
        return self.stack
        
        

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1
        

    def increment(self, k: int, val: int) -> None:
        # if k < len(self.stack):
        #     for i in range(k):
        #         self.stack[i] += val
        # else:
        #     for i,_ in enumerate(self.stack):
        #         self.stack[i] += val
        
        inc_no = min(k,len(self.stack))
        for i in range(inc_no):
            self.stack[i] += val
        return self.stack


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(1)
print(obj.stack)
# param_2 = obj.pop()
# obj.increment(k,val)