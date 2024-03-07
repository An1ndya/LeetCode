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
            //middle goes next node
            middle = middle.next;
            //temp goes next 2nd node
            temp = temp.next.next;
        }
        //when temp end, middle have the middle or 2nd middle node
        return middle;    
    }
}