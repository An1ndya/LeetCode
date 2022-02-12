# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        prev=None
        temp=head
        while temp!=None:
            
            if temp.val==val:
                if prev!=None: 
                    prev.next=temp.next
                if head==temp:
                    head=temp.next
                    #prev should remain same, as we dont know about next value 
            else:          
                prev=temp
            temp=temp.next
                
        return head
            