# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #value of maximum path
        self.maxpath = 0
        def getmaxheight(node):
            #means parent is leaf
            if not node: return 0
            
            lh = getmaxheight(node.left)
            rh = getmaxheight(node.right)
            # path will be sum of heights of left and and right subtree
            # update maximum path
            self.maxpath = max(self.maxpath, lh+rh )
            #return maximum height of left or right sub tree
            #parent is one node, so add 1 
            return max(lh,rh)+1
        #max height of root of no use to our answer
        #this recusive DFS call will check path on each node and update maximum path
        mxh = getmaxheight(root)
        
        return self.maxpath