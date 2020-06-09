# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 16:06:38 2019

@author: stevie
"""
def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1
        
    

haystack = "hello"
needle = "ll"
a = strStr(haystack,needle)
print(a)

