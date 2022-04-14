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
# @param {Integer} val
# @return {TreeNode}
def search_bst(root, val)
    if root==nil; return nil end
    if root.val==val; return root end
    ans=search_bst(root.left, val)
    if ans!=nil; return ans end
    ans=search_bst(root.right, val)
    if ans!=nil; return ans end
    return nil
end