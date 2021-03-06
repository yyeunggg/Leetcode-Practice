# -*- coding: utf-8 -*-
"""
Created on Sat May 30 13:16:51 2020

@author: steve
"""

"""
290. Word Pattern

"""

def wordPattern(pattern,string):
    pat_dict = {}
    word_dict = {}
    words = string.split()

    if pattern == string and len(pattern)!= 1:  #Identical strings, except for 'a':'a'
        return False
    elif len(pattern) != len(words):   #Mismatch of words
        return False
    
    for index, word in enumerate(words):
        try:    #For not equal length
            pat = pattern[index]
            if (pat not in pat_dict) and (word not in word_dict):   #Not in dictionary
                pat_dict[pat] = word
                word_dict[word] = pat
            else:
                try:    #For extra pattern or word
                    if (pat_dict[pat] == word) and (word_dict[word] == pat):    
                        pass
                    else:
                        return False
                except:
                    return False
        except:
            return False
        
    return True
    
pattern = "abba"
string = "dog cat cat dog"

# pattern = "e"
# string = "eukera"

# pattern = "deadbeef"
# string = "d e a d b e e f"


# pattern = "abba"
# string = "dog cat cat fish"

# pattern = "abba"
# string = "dog dog dog dog"

# pattern = "aaa"
# string = "aa aa aa aa"

# pattern = "jquery"
# string  = "jquery"

# pattern = 'he'
# string = 'unit'

print(wordPattern(pattern,string))