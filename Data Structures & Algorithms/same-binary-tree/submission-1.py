# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isSameTree = True
        
        def find_similarity(p,q):
            if p == q and p is None:
                pass

            elif type(p) == type(q) and type(p) == TreeNode:
                if p.val != q.val:
                    self.isSameTree = False

                pleft, qleft = p.left, q.left
                pright, qright = p.right, q.right

                find_similarity(pleft,qleft)
                find_similarity(pright,qright)


            else:
                self.isSameTree = False
            # if p.val != q.val:
            #     self.isSameTree = False

            # pleft, qleft = p.left, q.left
            # pright, qright = p.right, q.right

            # find_similarity(pleft,qleft)
            # find_similarity(pright,qright)

        find_similarity(p,q)
        return self.isSameTree        