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
# @return {Boolean}
def is_valid_bst(root)
    $prev =nil
    return is_bst(root) 
end
def is_bst(root)
    if root ==nil ; return true end

    if !is_bst(root.left) ; return false end
    #inorder traversal 
    if $prev!=nil and root.val <= $prev.val; return false end
    $prev  = root
    
    if !is_bst(root.right) ; return false end
    return true
end