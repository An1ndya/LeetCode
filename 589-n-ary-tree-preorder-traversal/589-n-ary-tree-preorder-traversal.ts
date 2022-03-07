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

function preorder(root: Node | null): number[] 
{
    let arr: number[]=[];
    DFS(root);
    return arr;
    
    function DFS(root: Node | null)
    {
        if(root===null){ return null;}
        arr.push(root.val);
        for(var child of root.children)
        {
            DFS(child);
        }
    };  
};