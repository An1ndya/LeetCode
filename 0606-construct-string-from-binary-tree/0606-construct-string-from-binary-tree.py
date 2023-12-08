# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.ans = ""
        
        def preorder( root: Optional[TreeNode]) -> None:
            if root==None: return
            
            self.ans+=str(root.val)           
            if root.right or root.left:      
                self.ans+="("
                preorder(root.left)
                self.ans+=")"
            if root.right :
                self.ans+="("
                preorder(root.right)
                self.ans+=")"
            return
            
        preorder(root)
        return self.ans