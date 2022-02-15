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

def preorder_traversal(root)
    $arr = []
    preorder(root)
    return $arr
end
def preorder(node)
    if node==nil; return nil end
    
    $arr.push(node.val)
        
    preorder(node.left)
    preorder(node.right)   
end