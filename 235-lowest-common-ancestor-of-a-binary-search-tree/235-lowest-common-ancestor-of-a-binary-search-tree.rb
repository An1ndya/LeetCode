# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @param {TreeNode} p
# @param {TreeNode} q
# @return {TreeNode}
def lowest_common_ancestor(root, p, q)
    min,max=[p.val,q.val].min,[p.val,q.val].max
    return common_ancestor(root, min,max)
end
def common_ancestor(root, p, q)
    if root==nil; return nil end
    if root.val >= p and root.val <= q; 
        return root 
    elsif root.val > p and root.val > q; 
        return common_ancestor(root.left, p, q)
    elsif root.val < p and root.val < q; 
        return common_ancestor(root.right, p, q)
    end
    
end