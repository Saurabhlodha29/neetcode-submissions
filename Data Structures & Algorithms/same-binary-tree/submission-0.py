# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: Both nodes are null, meaning we reached the end of identical branches
        if not p and not q:
            return True
        
        # Base case 2: One node is null and the other is not, or their values mismatch
        if not p or not q or p.val != q.val:
            return False
        
        # Recursive step: Check if both left and right subtrees match perfectly
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
