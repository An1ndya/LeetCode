# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=m=head
        prev=None
        while t !=None and t.next!=None:
            prev=m
            m=m.next
            t=t.next.next
        if prev!=None: 
            prev.next=m.next
            return head
        else:
            return None