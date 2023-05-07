'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
'''

# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        def inorder(root):
            if not root: 
                return
            
            inorder(root.left)
            ret.append(root.val)
            inorder(root.right)
        inorder(root)
        return ret
