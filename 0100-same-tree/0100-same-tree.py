# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None: 
            #no child, terminate match previous cases
            return True 
        elif p is None : 
            #q have child and p dont so not same 
            return False
        elif q is None : 
            # p have child and q dont so not same
            return False
        #check if value matched and same recursive check for left and right sub tree
        return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        