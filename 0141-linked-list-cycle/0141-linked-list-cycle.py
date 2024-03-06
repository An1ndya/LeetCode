# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        while temp!=None:
            if temp.val==100001:
                return True
            temp.val=100001
            temp=temp.next
        return False 