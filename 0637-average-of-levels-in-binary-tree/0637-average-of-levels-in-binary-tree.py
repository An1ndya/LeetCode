# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans=[]
        q=[]
        q.append(root)
        while q:
            sum =0
            n=len(q)
            for i in range(n):
                
                node=q.pop(0)
                sum += node.val
                
                if node.left : q.append(node.left)
                if node.right : q.append(node.right)
                    
            ans.append(sum/n)
        return ans
                
            