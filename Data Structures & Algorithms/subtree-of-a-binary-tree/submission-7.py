# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def preorder(node):
            if node is None:
                return ["#"]
            
            return [str(node.val)] + preorder(node.left) + preorder(node.right)

        main_str = "," + ",".join(preorder(root)) + ","
        sub_str = "," + ",".join(preorder(subRoot)) + ","

        return sub_str in main_str
                
            