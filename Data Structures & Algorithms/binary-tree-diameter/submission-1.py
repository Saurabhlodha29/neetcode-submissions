# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.diameter = 0

        def find_max_depth(root):
            if root == None:
                return 0

            leftHeight = find_max_depth(root.left)
            rightHeight = find_max_depth(root.right)

            self.diameter = max(self.diameter,leftHeight + rightHeight)


            return 1 + max(leftHeight,rightHeight)

        find_max_depth(root)

        return self.diameter