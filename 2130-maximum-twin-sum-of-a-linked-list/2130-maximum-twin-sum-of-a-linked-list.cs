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
    public int PairSum(ListNode head) {
        ListNode temp = head;
        int n=0,i=0,max=0,sum;
        
        while(temp!=null)
        {
            temp=temp.next;
            n++;
        }
        int[] arr = new int[n];
        temp = head;
        while(temp!=null)
        {
            arr[i] = temp.val; 
            temp=temp.next;
            
            i++;
        }
        for(i=0;i<n;i++)
        {
            sum = arr[i] + arr[n-1-i];
            if( sum> max) max = sum;
        }
        return max;
    }
}