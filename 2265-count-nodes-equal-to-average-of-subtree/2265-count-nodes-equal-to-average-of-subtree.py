# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
    
        self.ans=0
        self.DFS(root)
        return self.ans
    def DFS(self, root: Optional[TreeNode]):
        if not root: return 0,0
        
        suml,nl=self.DFS(root.left)
        sumr,nr=self.DFS(root.right)
        
        sum=root.val+suml+sumr
        n=nl+nr+1
        if root.val==sum//n: 
            #print(root.val)
            self.ans+=1
        
        return sum,n
        