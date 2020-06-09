# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:20:56 2020

@author: steve
"""



"""
744. Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/


"""


def nextGreatestLetter(letters,target):
    lo = 0
    hi = len(letters)

    if target >= letters[-1] or target < letters[0]:
        return letters[0]

    while lo != hi:
        mid = (lo + hi)//2
        if letters[mid] > target:
            if letters[mid-1] > target: 
                hi = mid
            else:
                return letters[mid]
        else:
            if letters[mid + 1] <= target:      
                lo = mid
            else:
                return letters[mid+1] 
    
    
    




letters = ["c", "f", "j"]
target = "k"

letters = ["e","e","e","k","q","q","q","v","v","y"]
targets = "k"

print(nextGreatestLetter(letters,target))