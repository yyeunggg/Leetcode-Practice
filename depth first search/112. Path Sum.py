# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:35:40 2020

@author: steve
"""

"""
112. Path Sum
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:    #Empty
            return False
        
        self.stack = [root]
        self.visited ={}
        root.sum = root.val
        
        while self.stack:
            cur_node = self.stack[-1]
            
            if cur_node.left and (cur_node.left not in self.visited):   #if there exist a value for left and it is not visited, we will use this
                self.stack += [cur_node.left]
                self.visited[cur_node.left] = 1
                cur_node.left.sum = cur_node.sum + cur_node.left.val
                
            elif cur_node.right and (cur_node.right not in self.visited):
                self.stack += [cur_node.right]
                self.visited[cur_node.right] = 1
                cur_node.right.sum = cur_node.sum + cur_node.right.val
                
            # It is a leaf if no leave exist. Means if not (cur_node.right or cur_node.left):
            elif  not (cur_node.right or cur_node.left):
                if cur_node.sum == sum:
                    return True
                self.stack.pop(-1)
             
            else:   #This includes both visited or one visited, the other empty.
                self.stack.pop(-1)
                
        return False
    
    
# Another way is to use dynamic programming
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        if not root:    #Empty
            return False
        
        self.check = sum
        self.result = False

        # Can use dynamic programming
        def check_sum(node,parent_sum):
            result = False
            node.sum = parent_sum + node.val
            
            if not (node.left or node.right):   #This is the case when it's a leaf
                result = node.sum == self.check
                return result
            
            if (node.left != None):
                result = check_sum(node.left,node.sum)
            if (not result) and (node.right != None):
                result = check_sum(node.right,node.sum)
                
            return result

        return check_sum(root,0)
    