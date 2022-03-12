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

function getDecimalValue(head: ListNode | null): number 
{
    let temp = head;
    let n =0;
    let p =1;
    let val=0;
    while(temp!=null)
    {
        n++;
        p*=2;
        temp=temp.next;
    }
    temp = head;
    while(temp!=null)
    {
        p/=2;
        val+=p*temp.val;
        temp=temp.next;
    }
    return val;
};