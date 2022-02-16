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
def is_symmetric(root)
    return is_mirror(root.left, root.right)
end
def is_mirror(node1, node2)
    if node1==nil and node2==nil 
        return true
    elsif node1==nil or node2==nil 
        return false 
    elsif node1.val!=node2.val
        return false
    end
    
    return (is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left))
end