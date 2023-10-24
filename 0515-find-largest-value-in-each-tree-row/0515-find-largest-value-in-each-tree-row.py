# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans=[]
        q=[root]
        while q:
            n=len(q)
            max=-(2**31)
            for i in range(n):
                node=q.pop(0)
                if node.val>max: max=node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(max)
        return ans