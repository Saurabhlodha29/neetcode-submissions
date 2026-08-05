# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # A None subRoot is always a subtree of any tree
        if not subRoot: 
            return True
        # If the main tree is empty but subRoot is not, it can't be a subtree
        if not root: 
            return False
        
        # If the current trees are identical, return True
        if self.isSameTree(root, subRoot):
            return True
        
        # Recurse down the left and right children of the main tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, they are identical
        if not p and not q:
            return True
        # If one node is None and the other isn't, or values don't match, they aren't identical
        if not p or not q or p.val != q.val:
            return False
        
        # Check if both left and right subtrees match exactly
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
