# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        level = 0 
        while queue:
            n = len(queue)
            #initilaize previous node as empty
            prev = None
            #same row wise node will be poped inside this loop
            for i in range(n):
               
                node = queue.pop(0)
                #print(prev.val,node.val)
                #even indexed level
                if level % 2 == 0:
                    # check if odd or not 
                    if node.val % 2 != 1: return False
                    #check if increasing order or not 
                    if prev:
                        if node.val <= prev.val : return False
                else:
                    # check if even or not 
                    if node.val % 2 != 0: return False
                    #check if increasing order or not 
                    if prev:
                        if node.val >= prev.val : return False 
                #update prev 
                prev = node
                #left child have to be put in queue first
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)  
            level+=1 
        return True