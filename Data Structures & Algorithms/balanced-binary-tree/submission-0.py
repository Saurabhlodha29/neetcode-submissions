# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_height(node: Optional[TreeNode]) -> int:
            # Base case: an empty tree has a height of 0
            if not node:
                return 0
            
            # Check the height of the left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
                
            # Check the height of the right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            # If the current node is unbalanced, propagate -1 upwards
            if abs(left_height - right_height) > 1:
                return -1
                
            # Return the actual height of the current node's subtree
            return 1 + max(left_height, right_height)
            
        return check_height(root) != -1
