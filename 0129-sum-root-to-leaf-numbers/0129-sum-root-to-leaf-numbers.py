# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        def DFS(node: Optional[TreeNode], sum:int)->None:
            nonlocal ans
            if node == None : 
                return
            elif node.left == None and node.right == None :
                #leaf node, so add to total sum
                #The previous sum * 10 as node value adding after last digit
                ans+= sum*10+node.val
                return
            #during traverse keep track of sum
            DFS(node.left, node.val+sum*10)
            DFS(node.right, node.val+sum*10)
            
            return 
        DFS(root,0)
        return ans