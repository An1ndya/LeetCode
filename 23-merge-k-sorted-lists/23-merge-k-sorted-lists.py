# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        prev=None
        head=None
        q = PriorityQueue()
        while len(lists)>0:
            i=0
            while i < len(lists):
                if lists[i]:
                    q.put(lists[i].val)
                    lists[i]=lists[i].next
                    i+=1
                else:
                    lists.pop(i)     
            
        while not q.empty():
            if prev:
                new = ListNode(q.get())
                prev.next=new
                prev=new
            else:
                new = ListNode(q.get())
                head=new
                prev=new

        return head
            
            
            
            