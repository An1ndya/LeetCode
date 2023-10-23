# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        fast=slow=prev=head
        #print(head)
        while fast and fast.next:
            prev = slow
            slow=slow.next
            fast=fast.next.next
            
        prev.next=None
        
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeList(l1,l2)
    
    def mergeList(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode(0)
        
        cur = head
        
        while  l1 and l2:
            if l1.val<=l2.val:
                cur.next=l1
                l1 = l1.next
            else:
                cur.next=l2
                l2 = l2.next   
            cur=cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return head.next
        
        