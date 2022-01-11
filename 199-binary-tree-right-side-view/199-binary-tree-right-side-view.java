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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ans = new LinkedList<>();
        Queue<TreeNode> q = new LinkedList<>();
        int size;
        if(root!=null) q.add(root);
        
        while(!q.isEmpty())
        {
            size = q.size();
            for(int i=0;i<size;i++)
            {
                TreeNode current = q.peek();
                q.poll();
                if(i==size-1) ans.add(current.val);
                if(current.left!=null) q.add(current.left);
                if(current.right!=null) q.add(current.right);
            }
        }
        return ans;
    }
}