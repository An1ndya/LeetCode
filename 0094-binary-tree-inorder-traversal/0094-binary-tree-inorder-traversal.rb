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
# @return {Integer[]}
def inorder_traversal(root)
    arr = []
    inorder(root,arr)
    return arr
end
def inorder(node,arr)
    if node==nil; return nil end
    
    inorder(node.left, arr)
    arr.push(node.val)
    inorder(node.right, arr)      
end