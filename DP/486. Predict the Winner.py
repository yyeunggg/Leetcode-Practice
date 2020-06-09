# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 21:29:25 2020

@author: steve
"""

"""
486. Predict the Winner
https://leetcode.com/problems/predict-the-winner/

"""

def PredictTheWinner(nums):
    
    score = {}
    
    if len(nums) % 2 ==0:
        return True
    
    def find_best_score(array,score):
        array_set = tuple(array)
        if array_set in score:
            return score[array_set]
        
        ## The bottom case
        if len(array) == 1:
            result = [array[0],0]
            score[array_set] = result
            return result
        elif len(array) == 2:
            result = [max(array),min(array)]
            score[array_set] = result
            return result
        
        ## General Case
        res1_ = find_best_score(array[1:],score)
        res1 = array[0] + res1_[1]
        
        res2_ = find_best_score(array[:-1],score)
        res2 = array[-1] + res2_[1]
        
        if res1 > res2: #We should choose the first value
            result = [res1,res1_[0]]
        else:   #We should choose the last value
            result = [res2,res2_[0]]
    
        score[array_set] = result
        return result
    
    answer = find_best_score(nums,score)
    # print(score)
    if answer[0]>=answer[1]:
        return True
    else:
        return False
    
    
nums = [1, 5, 233, 6]
nums = [1,3,1]
print(PredictTheWinner(nums))