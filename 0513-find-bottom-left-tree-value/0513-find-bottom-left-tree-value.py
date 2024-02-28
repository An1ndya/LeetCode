# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        while queue:
            n = len(queue)
            #first one is leftmost one
            #last row will executed last
            ans = queue[0].val
            #same row wise node will be poped inside this loop
            for i in range(n):
                node = queue.pop(0)
                #left child have to be put in queue first
                #so the first element in rowwise traversal will be leftmost 
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)   
        return ans