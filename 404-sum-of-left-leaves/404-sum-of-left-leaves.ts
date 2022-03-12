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

function sumOfLeftLeaves(root: TreeNode | null): number {
    
    if(TreeNode==null) return 0;
    
    return DFS(root, false);
};
function DFS(root: TreeNode , isleft: boolean): number 
{
    if(root==null) return 0;
    if(root.left==null && root.right==null && isleft) return root.val;
    return DFS(root.left, true) + DFS(root.right, false);
};