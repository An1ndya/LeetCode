"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None: 
            return None;
        d={head: Node(head.val)}
        
        stack=[head]
        while stack: 
            nd=stack.pop()
            if nd.next !=None:
                if nd.next not in d:
                    d[nd.next]= Node(nd.next.val)
                    stack.append(nd.next)
                d[nd].next = d[nd.next]
            if nd.random !=None:
                if nd.random not in d:
                    d[nd.random]= Node(nd.random.val)
                    stack.append(nd.random)
                d[nd].random = d[nd.random]
        return d[head]