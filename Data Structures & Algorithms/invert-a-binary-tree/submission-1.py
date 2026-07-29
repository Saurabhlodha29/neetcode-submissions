class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        leftSubtree = self.invertTree(root.left)
        rightSubtree = self.invertTree(root.right)

        root.left = rightSubtree
        root.right = leftSubtree

        return root
        

        
