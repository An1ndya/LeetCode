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
# @return {Integer}
def max_depth(root)
    return DFS(root,0)
end
def DFS(node, d)
    if node==nil
        return d
    end
    return max(DFS(node.left,d+1),DFS(node.right,d+1))
end
def max (a,b)
  a>b ? a : b
end