# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:43:19 2020

@author: steve
"""

"""

1456. Maximum Number of Vowels in a Substring of Given Length

"""

def maxVowels(s,k):
    vowels = {'a','e','i','o','u'}
    max_vol = 0
    vol_cur_win = 0
    
    for i in range(k):
        if s[i] in vowels:
            vol_cur_win += 1
    max_vol = vol_cur_win
    

    for i in range(1,len(s)-k+1):
        if s[i+k-1] in vowels:
            vol_cur_win += 1
        if s[i-1] in vowels:
            vol_cur_win -= 1
        if max_vol < vol_cur_win:
            max_vol = vol_cur_win
            
    return max_vol
        
    
    
    
    
    
    


# s = "abciiidef"
# k = 3

s = "rhythms"
k = 4

s = "leetcode"
k = 3

print(maxVowels(s,k))