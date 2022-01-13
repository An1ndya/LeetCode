/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode{
    
    var temp1 *ListNode = list1
    var temp2 *ListNode = list2
    var mergedhead *ListNode = nil
    var merged *ListNode
    var cur *ListNode
    var count int = 0
    for temp1!= nil || temp2!= nil {
        if temp1!= nil && temp2!= nil {
            if temp1.Val < temp2.Val{
                cur = &ListNode{temp1.Val,nil}

                temp1 = temp1.Next 
            }else{
                cur = &ListNode{temp2.Val,nil}
                temp2 = temp2.Next 
            }
        }else if temp1 != nil {
            cur = &ListNode{temp1.Val,nil}
            temp1 = temp1.Next 
        }else if temp2 != nil {
            cur = &ListNode{temp2.Val,nil}
            temp2 = temp2.Next
        }
        if count == 0 { 
            mergedhead = cur
            merged = mergedhead
        }else{
            merged.Next = cur
            merged = merged.Next 
        }
        count++
    }

    return mergedhead
}