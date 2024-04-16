# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        #base case
        if depth == 1:
            newroot = TreeNode(val)
            newroot.left = root
            return newroot
        queue = deque([root])
        level = 0
        while queue: 
            level += 1
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                #new level should be instered as child of node having depth - 1
                if level == depth -1:
                    leftchild  = node.left
                    rightchild = node.right
                    node.left = TreeNode(val)
                    node.left.left = leftchild
                    node.right = TreeNode(val)
                    node.right.right = rightchild
                else:
                    #procced like BFS
                    if node.left: 
                        queue.append(node.left)
                    if node.right: 
                        queue.append(node.right)
            if level == depth -1: 
                break
        return root
                    
                
        