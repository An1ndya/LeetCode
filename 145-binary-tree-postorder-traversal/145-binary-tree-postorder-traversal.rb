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
def postorder_traversal(root)
    if root==nil; return [] end
    arr=[]
    arr += postorder_traversal(root.left)
    arr += postorder_traversal(root.right)
    arr << root.val
    return arr
end