# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:14:56 2019

@author: steve
"""

def maxNumberOfBalloons(text):
    letter_count = {}
    for letter in 'balloon':
        letter_count[letter] = text.count(letter)
#    print(letter_count)
    letter_count['l'] //= 2
    letter_count['o'] //= 2
    maximum = min(letter_count.values())
#    print(letter_count)
    return maximum

text = "nlaebolko"
ans = maxNumberOfBalloons(text)
print(ans)