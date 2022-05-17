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

function getTargetCopy(original: TreeNode | null, cloned: TreeNode | null, target: TreeNode | null): TreeNode | null 
{
    if(original == null ) return null;
    if(original == target) return cloned;
    
    let left = getTargetCopy(original.left,cloned.left,target);
    if(left!=null) return left;
    let right = getTargetCopy(original.right,cloned.right,target);
    if(right!=null) return right;
};