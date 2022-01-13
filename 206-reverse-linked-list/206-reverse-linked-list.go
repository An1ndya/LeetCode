/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    //var reversehead *ListNode = nil
    var prev, next, cur *ListNode;
    cur = head
    prev = nil
    for cur!=nil{
        next = cur.Next
        cur.Next = prev
        prev = cur
        cur = next
    }
    head = prev
    return head
}