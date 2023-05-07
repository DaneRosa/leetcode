'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
'''

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
class Solution: 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a = []
        b = []

        def inorder(root, x):
            if not root: 
                return False
            
            inorder(root.left, x)
            x.append(root.val)
            inorder(root.right, x)
        inorder(p,a)
        inorder(q,b)

        return a == b


        