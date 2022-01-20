/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    var prev, temp *ListNode
    
    temp = head
    prev = nil
    isduplicate := false
    
    for temp != nil{
        
        for temp.Next!= nil && temp.Val == temp.Next.Val{
            temp = temp.Next
            isduplicate = true
        }
        if isduplicate{
            if prev == nil{
                head = temp.Next
            }else{
                prev.Next = temp.Next
            }
            isduplicate = false
        }else{
            prev = temp
        }
        temp = temp.Next
    }
    return head
}