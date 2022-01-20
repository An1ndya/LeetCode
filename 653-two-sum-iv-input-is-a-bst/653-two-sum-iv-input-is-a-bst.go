/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */




func findTarget(root *TreeNode, k int) bool {
    
     m := make(map[int]bool)
    
    return traverse(root,k,m)
}

func traverse(node *TreeNode, k int, m map[int]bool) bool{
    
    if node == nil {return false}
    
    complement := k-node.Val
    
    if m[complement] {return true}
    
    m[node.Val] = true
    
    left, right := node.Left, node.Right
    
    return traverse(left,k,m) || traverse(right,k,m)
}