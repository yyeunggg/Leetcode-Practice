# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:06:50 2020

@author: steve
"""


"""
67. Add Binary

"""

# Turn string into binary
def addBinary(a,b):
    ans = bin(int(a,2)+int(b,2))
    return ans[2:]


a = "11"
b = "1"

print(addBinary(a,b))