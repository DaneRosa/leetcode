# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            # helper function to check if two trees are mirrors
            def isMirror(t1, t2):
                # if both trees are empty, they are mirrors
                if not t1 and not t2: 
                    return True
                # if only one tree is empty, they are not mirrors
                if not t1 or not t2: 
                    return False
                # check if the current nodes are mirrors and if their subtrees are mirrors
                return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
            # call the helper function on the root twice to check if the tree is symmetric
            return isMirror(root, root)
    
# faster: 
'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Return the function recursively...
        return self.isSame(root.left, root.right)
    # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
    def isSame(self, leftroot, rightroot):
        # If both root nodes are null pointers, return true...
        if leftroot == None and rightroot == None:
            return True
        # If exactly one of them is a null node, return false...
        if leftroot == None or rightroot == None:
            return False
        # If root nodes haven't same value, return false...
        if leftroot.val != rightroot.val:
            return False
        # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)
'''