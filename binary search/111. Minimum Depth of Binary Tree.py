# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:54:56 2020

@author: steve
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

#[3,9,20,null,null,15,7]

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        stack = [root]
        length = 10000
        nogo = set()
        depth = {}
        depth[root] = 1
    
        if not root:
            return 0
    
        while stack:            
            node = stack[-1]
            # print(node.val)

            try:
                node_depth = depth[node]
            except:
                node_depth = depth[stack[-2]] + 1
                depth[node] = node_depth
              
            if not (node.left or node.right):    # Time to compare if it is a dead end
                nogo.add(node)
                if node_depth < length:
                    length = node_depth
                stack.pop()  # Pop last item of stack
                continue
                    
            if node.left and (node.left not in nogo):
                stack.append(node.left)
                
            elif node.right and (node.right not in nogo):
                stack.append(node.right)
                
            else:
                stack.pop()
                nogo.add(node)

            
        return length
            

            
        