# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1leaf=[]
        root2leaf=[]
        def DFS(root,leaf):
            if not root.left  and not root.right:
                #leaf node
                leaf.append(root.val)
        
            if root.left:
                DFS(root.left,leaf)
            if root.right:
                DFS(root.right,leaf)
                
        DFS(root1,root1leaf)
        DFS(root2,root2leaf)
        
        if len(root1leaf) != len(root2leaf):
            return False
        for i in range(len(root1leaf)):
            if root1leaf[i] != root2leaf[i]:
                return False
        return True
        
        
                
                