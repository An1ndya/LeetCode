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
    public ListNode MiddleNode(ListNode head) {
        ListNode temp,middle;
        middle = head;
        temp = head;
        while(temp != null && temp.next != null)
        {
            middle = middle.next;
            temp = temp.next.next;
        }
        return middle;    
    }
}