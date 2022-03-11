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

function rotateRight(head: ListNode | null, k: number): ListNode | null 
{
    let n = 0;
    let temp = head;
    let tail = null;
    let prev = null;
    while(temp!=null)
    {   
        n++;
        tail = temp;
        temp=temp.next;
    }
    k%=n;
    let i=0;
    temp = head;
    while(temp!=null)
    {         
        if(i==n-k)
        {
            prev.next=null;
            tail.next= head;
            head=temp;
            break;
        }
        i++;
        prev=temp;
        temp=temp.next;
    }

    return head;
};