/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    //keep track of current , previous and next node
    var prev, next, cur *ListNode;
    cur = head
    prev = nil
    for cur!=nil{
        next = cur.Next
        //set next value to previous element
        //this process does for all node and list become reverse
        cur.Next = prev
        prev = cur
        cur = next
    }
    //prev is the last node
    head = prev
    return head
}