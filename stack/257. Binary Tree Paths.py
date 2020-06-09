# -*- coding: utf-8 -*-
"""
Created on Wed May 27 20:24:58 2020

@author: steve
"""

"""
257. Binary Tree Path
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Runtime: 28 ms, faster than 88.09% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 14.1 MB, less than 9.52% of Python3 online submissions for Binary Tree Paths.
"""

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return None
        
        string = str(root.val)
        self.path = []
        self.visited = []
        self.stack = [root]
        
        def check_exist_leaf(root):       
            # No leaf
            if (not root.left) and (not root.right):
                # print('no leaf')
                return True
            return False
        
        
        while self.stack:
            current_root = self.stack[-1]
            self.visited += [current_root]

            # Will recede to last root if it's a dead end
            # By checking if there exist leaf
            if check_exist_leaf(current_root):
                self.stack.pop()
                
            # Since it is the deepest, return to path and cencel last digits
                self.path += [string]
                string = string[0:-2 - len(str(current_root.val))]
                
            # If left branch exist and not visited
            elif (current_root.left not in self.visited) and current_root.left:
                self.stack += [current_root.left]
                
            # Append new path to string
                string += '->' + str(current_root.left.val)
                
            # If right branch exist and not visited
            elif (current_root.right not in self.visited) and current_root.right:
                self.stack += [current_root.right]
                
            # Append new path to string
                string += '->' + str(current_root.right.val)    
                
            # Both branches are visited
            else:
                self.stack.pop()
                string = string[0:-2 - len(str(current_root.val))]
        
        
            print(self.path)
            
        return self.path