# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.isBalanced = True

        def dfs(root):
            if root is None:
                return 0
            
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)
        
            if abs(leftHeight - rightHeight) > 1:
                self.isBalanced = False

            return 1 + max(leftHeight,rightHeight)

        dfs(root)
        return self.isBalanced