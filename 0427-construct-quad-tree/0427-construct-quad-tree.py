"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid: return None
        n = len(grid)
        sum=0
        for i in range(n):
            for j in range(n):
                sum+=grid[i][j]
                    
        if sum==0 or sum==n*n:
            return Node(bool(grid[0][0]),True,None,None,None,None)
        
        mid=n//2
        
        return Node(False, False,
        self.construct([grid[i][0:mid] for i in range(0,mid)]),
        self.construct([grid[i][mid:n] for i in range(0,mid)]),
        self.construct([grid[i][0:mid] for i in range(mid,n)]),
        self.construct([grid[i][mid:n] for i in range(mid,n)]))