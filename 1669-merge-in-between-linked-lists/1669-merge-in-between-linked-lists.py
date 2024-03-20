# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        n=0
        prevA = None # previous of a th node
        NextB = None # next of b th node
        
        node = list1
        while node:  
            if n == a:
                #node is a th node, save prev node
                prevA = prev
            if n == b:
                #node is b th node, save next node
                NextB = node.next
                break
            prev = node
            node = node.next
            n+=1
        
        
        lastnode = list2
        #traverse so lastnode will be the last node of list2
        while lastnode.next:
            lastnode = lastnode.next
        #to remove node a to b we just need 
        #set prevA.next as list2's first node
        prevA.next = list2
        #set lastnode.next as NextB
        lastnode.next = NextB
        
        return list1