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
def insert_into_bst(root, val)
    if root==nil ; return TreeNode.new(val,nil,nil) end
    insert(root, nil, val)
    return root
end
def insert(root, par, val)
    if root==nil; 
        if par.val > val 
            par.left = TreeNode.new(val,nil,nil)
        else
            par.right = TreeNode.new(val,nil,nil)
        end
        return 
    end
    if root.val > val
        return insert(root.left,root,val)
    else
        return insert(root.right,root, val)
    end
end