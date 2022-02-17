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
# @param {Integer} target_sum
# @return {Boolean}
def has_path_sum(root, target_sum)   
    return DFS(root, 0, target_sum)
end
def DFS(node, sum, target_sum)
    if node == nil ; return false end   
    sum+=node.val
    if node.left ==nil and  node.right==nil
        if target_sum == sum 
            return true 
        else
            return false
        end
    else
        return (DFS(node.left,sum,target_sum) or DFS(node.right, sum, target_sum))
    end  
end