# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        def DFS(node):
            nonlocal carry
            if not node: return 
            next = node.next
            DFS(next)
            val= node.val*2 + carry
            node.val = val%10
            carry = val//10
        DFS(head)
        if carry > 0:
            head =  ListNode(carry,head)
        return head
            