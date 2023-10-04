# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        temp=head
        left = None
        right = None
        ans = None
        righthead = None
        while temp:
            if temp.val<x:
                if left == None: 
                    left = ListNode(temp.val)
                    ans = left
                else: 
                    left.next = ListNode(temp.val)
                    left=left.next
            else:
                if right == None: 
                    right = ListNode(temp.val)
                    righthead = right
                else: 
                    right.next = ListNode(temp.val)
                    right=right.next
            temp=temp.next
        #print(ans)
        #print(righthead)
        if ans:
            left.next = righthead
        else:
            ans = righthead
        return ans