# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def DFS(node, arr):
            nonlocal count
            arr[node.val]+=1
            if not node.right and not node.left:
                #leaf node
                #check if pseudo-palindromic
                ispseudo = True
                pathlen = sum(arr)
                for numcount in arr:
                    if numcount%2==1:
                        if pathlen%2==1:
                            #set odd path length to even
                            #so next odd count dont fit
                            pathlen -=1   
                        else:
                            # not pseudo-palindromic
                            ispseudo = False
                            break
                if ispseudo: count+=1
            else:
                
                if node.left: DFS(node.left,arr)
                if node.right: DFS(node.right,arr) 
            #backtracking 
            #list in ptyhon call by reference
            arr[node.val]-=1
        count=0       
        arr = [0 for i in range(10)]          
        DFS(root, arr)
        return count
                