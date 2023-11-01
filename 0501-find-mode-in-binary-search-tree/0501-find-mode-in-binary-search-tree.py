# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        self.cur = 0
        self.curCounter = 0
        self.maxCounter = 0
        self.DFS(root)
        return self.ans
    
    def DFS(self, root: Optional[TreeNode]) -> None:
        if not root: return None
        
        self.DFS(root.left)
        
        
        if self.cur==root.val:
            self.curCounter+=1
        else:
            self.curCounter=1
            self.cur=root.val
    
        if self.curCounter > self.maxCounter:
            self.maxCounter = self.curCounter
            self.ans=[]
        
        if self.curCounter == self.maxCounter:
            self.ans.append(root.val) 
            
        
        
        self.DFS(root.right)
        
        return None