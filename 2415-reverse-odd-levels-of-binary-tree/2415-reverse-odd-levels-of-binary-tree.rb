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
def reverse_odd_levels(root)
    if root == nil; return nil end
    
    invert_tree_odd(root.left, root.right, true)   
    return root
end
def invert_tree_odd(left, right, booIsOdd) 
    
    if left == nil; return nil end
    
    if booIsOdd == true ;
        if left and right;
            left.val, right.val = right.val, left.val
        end
    end 
    invert_tree_odd(left.left, right.right, (not booIsOdd ))
    invert_tree_odd(left.right, right.left, (not booIsOdd ))
    
end
