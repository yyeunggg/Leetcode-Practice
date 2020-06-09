# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 22:26:23 2020

@author: steve
"""

"""
1306. Jump Game III

https://leetcode.com/problems/jump-game-iii/

"""

"""
Runtime: 252 ms, faster than 27.60% of Python3 online submissions for Jump Game III.
Memory Usage: 20.1 MB, less than 52.71% of Python3 online submissions for Jump Game III.
"""

def canReach(arr, start):
    que = [start]
    visited = {(arr[start],start)}
    
    while que:
        cur_index = que.pop(0)
        cur_val = arr[cur_index]
           
        left_index = cur_index - cur_val
        right_index = cur_index + cur_val
  

        if left_index >= 0:
            left_val = arr[left_index]
        
            if left_val == 0:
                return True
            
            if (left_val,left_index) not in visited:
                visited.add((left_val,left_index))
                que += [left_index]     

        
        if right_index < len(arr):
            right_val = arr[right_index]
            
            if right_val == 0:
                return True
                
            if (right_val,right_index) not in visited:
                visited.add((right_val,right_index))
                que += [right_index]


    return False
    
    
"""
Try to go faster
Runtime: 228 ms, faster than 95.86% of Python3 online submissions for Jump Game III.
Memory Usage: 20.1 MB, less than 51.04% of Python3 online submissions for Jump Game III.
"""

def canReach(arr, start):
    que = [start]
    visited = {start}
        
    while que:
        cur_index = que.pop(0)
        cur_val = arr[cur_index]
           
        left_index = cur_index - cur_val
        right_index = cur_index + cur_val
  

        if left_index >= 0:
            left_val = arr[left_index]
        
            if left_val == 0:
                return True
            
            if left_index not in visited:
                visited.add(left_index)
                que.append(left_index)     

        
        if right_index < len(arr):
            right_val = arr[right_index]
            
            if right_val == 0:
                return True
                
            if right_index not in visited:
                visited.add(right_index)
                que.append(right_index)


    return False



arr = [4,2,3,0,3,1,2]
start = 5

# arr = [4,2,3,0,3,1,2]
# start = 0

# arr = [3,0,2,1,2]
# start = 2

arr = [0,1]
start = 1

print(canReach(arr,start))