/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        int size = 0;
        ListNode temp, beforeRemovedOne;
        temp = head;
        beforeRemovedOne = null;
        while(temp != null)
        {
            temp = temp.next;
            size++;
        }
        if (size == 1) return null;  //avoid runtime error single element
        else if (size == n) return head.next;
        temp = head;
        while(size != n) // assign temp to remove node 
        {
            beforeRemovedOne = temp;
            temp = temp.next;
            size--;
        }
        beforeRemovedOne.next = temp.next;
        return head; 
        
    }
}