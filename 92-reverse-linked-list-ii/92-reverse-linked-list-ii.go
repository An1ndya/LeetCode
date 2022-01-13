/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseBetween(head *ListNode, left int, right int) *ListNode {
    var prev, next, cur, leftnode,beforeleftnode *ListNode;
    cur = head
    prev = nil
    beforeleftnode = nil
    var i int = 0 
    for cur!=nil{
        
        next = cur.Next
        
        if i == left -2{
            beforeleftnode = cur
        } else if i == left -1 {
            leftnode = cur
        }else if i >= left && i < right-1{
            cur.Next = prev
        } else if i == right-1{ 
            cur.Next = prev
 
            leftnode.Next = next
            
            if beforeleftnode != nil {
                beforeleftnode.Next = cur
            }else{
                //reverse start from first position
                head = cur
            }
            break      
        }   
        prev = cur
        cur = next
        i++
    }
    return head    
}