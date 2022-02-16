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
# @return {Integer[][]}
def level_order(root)
    ans=[]
    if root==nil; return ans end
    q=Queue.new
    q <<root
    while not q.empty?
        arr=[]
        n=q.length()
        for i in 1..n
            node=q.pop
            if node.left!=nil;  q<<node.left  end
            if node.right!=nil; q<<node.right end               
            arr << node.val
        end
        ans<<arr
    end
    ans
end