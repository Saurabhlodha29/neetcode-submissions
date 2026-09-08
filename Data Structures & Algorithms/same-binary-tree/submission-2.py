# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        similar = True
        
        def find_similarity(p,q):
            if not p and not q:
                pass

            elif p and q:
                if p.val != q.val:
                    return False

                leftResult = find_similarity(p.left,q.left)
                rightResult = find_similarity(p.right,q.right)

                if leftResult and rightResult:
                    return True
                else:
                    return False

            else:
                return False
            
            return True

        similar = find_similarity(p,q)
        return similar        