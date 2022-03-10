/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
        let  head=null;
        let  prev=null;

        let  add=0;
        while(l1!=null || l2!=null || add!=0)
        {
            let n=0;
            if(l1!=null && l2!=null)
            {
                n=l1.val+l2.val;
                l1=l1.next;
                l2=l2.next;
            }
            else if(l1!=null)
            {
                n=l1.val;
                l1=l1.next;
            }
            else if(l2!=null)
            {
                n=l2.val;
                l2=l2.next;
            }
            
            n+=add;
            //console.log(n);
            if(n>9)
            {
                add=float2int(n/10);
                n=n%10;
            }else{
                add=0;
            }
            let node = new ListNode(n);
            if(head==null)
            {
                head = node;           
            }
            else
            {
                prev.next= node;
            }
            prev = node; 
        }
        return head;
};
function float2int (value) {
    return value | 0;
}