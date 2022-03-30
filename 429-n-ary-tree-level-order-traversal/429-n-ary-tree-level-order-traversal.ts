/**
 * Definition for node.
 * class Node {
 *     val: number
 *     children: Node[]
 *     constructor(val?: number) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.children = []
 *     }
 * }
 */

function levelOrder(root: Node | null): number[][] 
{
    if(root==null) return [];
    let ans: number[][]=[];
    let stack: Node[]=[];
    stack.push(root);
    while(stack.length>0)
    {     
        let size = stack.length;
        let level : number[]=[];
        while(size>0)
        {
            let node = stack.shift();
            level.push(node.val);
            //console.log(node.val);
            for(var child of node.children)
            {
                stack.push(child);
            }
            size--;
        }
        ans.push(level);
    }
    return ans;	
};