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
let head=null;
let prev =null;
function increasingBST(root: TreeNode | null): TreeNode | null 
{
    head=null;
    prev =null;
    inOrder(root);
    return head;
};
function inOrder(root: TreeNode | null): null {
    if(root==null) return null;
    inOrder(root.left);   
    if(prev==null)
    {
        head = new TreeNode(root.val);
        prev=head;
    }else{
        prev.right = new TreeNode(root.val);
        prev=prev.right;
    }
    inOrder(root.right);
};