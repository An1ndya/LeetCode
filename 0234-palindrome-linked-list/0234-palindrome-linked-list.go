/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func isPalindrome(head *ListNode) bool {
    
    var cur,replicahead,temp,newnode *ListNode
    cur = head
    //a new linked list same as given one
    for cur!=nil{
        if replicahead == nil{ 
            
            newnode = &ListNode{cur.Val,nil}
            replicahead = newnode
            temp = replicahead
        }else{
            
            newnode = &ListNode{cur.Val,nil}
            temp.Next = newnode
            temp = temp.Next
        }
        cur = cur.Next
    }
    //reverse the linked list
    var reversed  = reverseList(replicahead)
   
    cur = head
    temp = reversed 
    //traverse both list and check if disimillar value found
    for cur!=nil{
        if cur.Val != temp.Val { 
            return false
        }
        cur = cur.Next
        temp = temp.Next
    }
  
    return true
}
func reverseList(head *ListNode) *ListNode{

    var prev, next, cur *ListNode
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
//display function for debugging 
func Display(list *ListNode) {
	for list != nil {
		fmt.Printf("%v ->", list.Val)
		list = list.Next
	}
	fmt.Println()
}