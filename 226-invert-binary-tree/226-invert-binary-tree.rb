# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {TreeNode}
def invert_tree(root) 
    DFS(root) 
    return root
end
def DFS(root)
    
    if root ==nil; return end
    
    left, right=root.left,root.right
    root.left,root.right = root.right, root.left

    DFS(root.left)
    DFS(root.right)
    
end