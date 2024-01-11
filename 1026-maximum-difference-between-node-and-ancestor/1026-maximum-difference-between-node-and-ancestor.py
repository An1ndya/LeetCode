# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mx =0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        mx = 0
        def DFS(node, maxvalue, minvalue):
            nonlocal mx
            if not node:
                return 
            mx = max(mx, abs(maxvalue-node.val))
            mx = max(mx, abs(minvalue-node.val))
            
            DFS(node.left, max(maxvalue,node.val), min(minvalue,node.val))
            DFS(node.right, max(maxvalue,node.val), min(minvalue,node.val))
           
        DFS(root,root.val,root.val)
        
        return mx