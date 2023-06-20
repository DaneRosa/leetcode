'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root: 
            # if root is null
            return False
        if not root.left and not root.right: 
            # if we are at leaf node
            return targetSum == root.val 
            # check if targetSum is equal to current node value
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val) 
        # recursively check left and right subtree

# The base case is the case where we reach the end of a path. 
# If the path sum is equal to the value of the node that we are currently on, then we return True. Otherwise, we return False.

# We call the recursive function on the left and the right children of the current node, 
# subtracting the value of the current node from the sum we are looking for. 
# If either of the two recursive calls return True, then we return True. Otherwise, we return False. 