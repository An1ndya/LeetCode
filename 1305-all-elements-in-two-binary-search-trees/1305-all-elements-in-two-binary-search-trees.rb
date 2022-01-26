# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root1
# @param {TreeNode} root2
# @return {Integer[]}
def get_all_elements(root1, root2)
    
    arr = []
    
    DFS(root1,arr)
    DFS(root2,arr)
    
    return arr.sort
end

def DFS(node,arr)
    
    return if node == nil 
    
    arr.push(node.val)
    
    DFS(node.left,arr)
    DFS(node.right,arr)

end