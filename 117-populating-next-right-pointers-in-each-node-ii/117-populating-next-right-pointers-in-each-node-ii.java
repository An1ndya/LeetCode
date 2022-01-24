/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root)
    {
        BFS(root);
        return root;
    }
    public void BFS(Node node)
    {
        if(node == null) return;
        Queue<Node> q = new LinkedList<>();
        int size;
        q.add(node);
        
        while(!q.isEmpty())
        {
            size = q.size();
            
            for(int i=0;i<size;i++)
            {
                Node current = q.peek();
                q.poll();
                //i=size-1 means most right side node of that level, so no need to update
                if(i<size-1) current.next = q.peek(); 
                if(current.left!=null) q.add(current.left);
                if(current.right!=null) q.add(current.right);
                
            }
        }
    }
}