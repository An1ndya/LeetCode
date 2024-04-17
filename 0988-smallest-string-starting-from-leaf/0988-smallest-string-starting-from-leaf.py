# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        smallest = None
        
        def DFS(node, string):
            nonlocal smallest
            
            if not node: return
            
            string = chr(node.val+97) + string
            #leaf node
            if not node.left and not node.right:
                # update if never updated or found smaller 
                if not smallest or smallest > string:
                    smallest = string
            if node.left:
                DFS(node.left, string) 
            if node.right:
                DFS(node.right, string) 
                
        DFS(root,"")
        return smallest