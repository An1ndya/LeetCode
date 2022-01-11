/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode mergeTrees(TreeNode root1, TreeNode root2)
    {
        TreeNode merged = MergeTrees(root1, root2);
        return merged;
    }
    /* Method to merge given two binary trees*/
     public TreeNode MergeTrees(TreeNode t1, TreeNode t2)
     {
         if (t1 == null)
             return t2;
         if (t2 == null)
             return t1;
         t1.val += t2.val;
         t1.left = MergeTrees(t1.left, t2.left);
         t1.right = MergeTrees(t1.right, t2.right);
         return t1;
     }
}