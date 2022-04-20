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

class BSTIterator {
    index: number;
    n :  number ; 
    stack: TreeNode[];
    constructor(root: TreeNode | null) 
    {
        this.stack = [];
        this.inOrder(root);
        this.index=0;
        this.n=this.stack.length;
    }

    next(): number 
    {
        let val= this.stack[this.index].val;
        this.index++;
        return val;
    }

    hasNext(): boolean {
        return this.index< this.n;
    }
    inOrder(root: TreeNode | null): void {
        if(root==null) return;
        this.inOrder(root.left);
        this.stack.push(root);
        this.inOrder(root.right);
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * var obj = new BSTIterator(root)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */