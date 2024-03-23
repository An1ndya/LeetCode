# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        linkedlist = [] #list of all node
        cur = head
        n=0
        while cur:
            linkedlist.append(cur)
            cur = cur.next 
            n += 1
        #break base case
        if n == 1: return head
        i=0
        for i in range(n//2):
            #link them according to solution
            linkedlist[i].next = linkedlist[n-1-i]
            linkedlist[n-1-i].next = linkedlist[i+1]
        #avoid cycle linked list, i+1's next is never set  
        #old link is i+1 -> i+2, we need sever that to break cycle
        linkedlist[i+1].next = None
        return head