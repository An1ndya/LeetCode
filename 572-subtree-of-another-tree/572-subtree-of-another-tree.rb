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
# @param {TreeNode} sub_root
# @return {Boolean}

def is_subtree(root, sub_root)
    return traverse(root, sub_root)
end

def is_sametree(root1, root2)
    
    if root1==nil && root2==nil
        return true
    elsif root1 != nil && root2 != nil
        if root1.val !=root2.val
            return false
        else     
            return is_sametree(root1.left,root2.left) && is_sametree(root1.right,root2.right)
        end
    else
        #one nil other not
        return false
    end         
end

def traverse(root, sub_root)
    
    if root==nil 
        return false
    end
    if is_sametree(root,sub_root) == true
        return true
    end 
    
    return traverse(root.left,sub_root)  ||  traverse(root.right,sub_root)
end