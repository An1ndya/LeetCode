/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isBalanced(root: TreeNode | null): boolean 
{
    if(root==null) return true;
    
    return height(root)!=-1;
};
function height(root: TreeNode | null): number 
{
    if(root==null) return 0;
    
    let left = height(root.left);
    
    if(left==-1) return -1;
    
    let right = height(root.right);
    
    if(right==-1) return -1;
    
    if(Math.abs(left-right)>1) return -1;
    
    return Math.max(left,right)+1;
}