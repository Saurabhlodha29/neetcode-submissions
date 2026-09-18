# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # def findSimilarity(p,q):
        #     if not p and not q:
        #         pass 
        #     elif p.val != q.val:
        #         return False
        #     else:
        #         return findSimilarity(p.left,q.left) and findSimilarity(p.right,q.right)

        
        def preorder(node):
            if node is None:
                return ["#"]
            
            return [str(node.val)] + preorder(node.left) + preorder(node.right)

        main_str = "," + ",".join(preorder(root)) + ","
        sub_str = "," + ",".join(preorder(subRoot)) + ","

        return sub_str in main_str
                
            