class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        
        n = len(citations)
        
        max=0
        
        for i in range(n):
            h= min(citations[i], n-i)
            if max < h  : max = h
        return max
            