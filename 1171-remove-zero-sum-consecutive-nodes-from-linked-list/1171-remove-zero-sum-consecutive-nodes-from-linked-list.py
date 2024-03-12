# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prefixSumtoNode = {}
        prefixSum = 0
        temp = dummy
        while temp:
            prefixSum += temp.val
            #update prefix sum to node
            #recurrent value will be replaced with last one
            prefixSumtoNode[prefixSum] = temp
            temp = temp.next
        prefixSum = 0
        temp = dummy
        while temp:
            prefixSum += temp.val
            #as same prefix sum means we found zero sum sequnce between them
            #temp.next and next same prefixsum node are in zero sum sequence
            #so update following to omit thus sequence
            #for other case both value is same 
            temp.next = prefixSumtoNode[prefixSum].next
            temp = temp.next
        return dummy.next