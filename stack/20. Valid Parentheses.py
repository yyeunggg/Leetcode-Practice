# -*- coding: utf-8 -*-
"""
Created on Tue May 26 20:13:27 2020

@author: steve
"""

"""
20. Valid Parentheses
"""


# Use stack
def isValid(s):
    pair = {'[' : ']', '(':')', '{':'}'}
    allow = ['[','(', '{']
    stack = []
    for symbol in s:
        if symbol in allow:
            stack += [symbol]
        else:
            try:
                if symbol == pair[stack[-1]]:
                    stack.pop(-1)
                else:
                    return False
            except:     #This is the case such as s = ']'
                    return False      
    if len(stack) == 0:
        return True
    else:
        return False
    
    
# Save a little bit of space
def isValid(s):
    pair = {'[' : ']', '(':')', '{':'}'}
    stack = []
    for symbol in s:
        if symbol in pair:  
            stack += [symbol]
        elif not stack:
            return False    #Empty
        elif symbol != pair[stack.pop()]:
            return False
    return not stack
        
        
    
s = "{[]}"
s = "([)]"
s = ']'
s = "()"
print(isValid(s))