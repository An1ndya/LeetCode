class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        t=0
        for i in left:
            t=max(t,i)
        for i in right:
            t=max(t, n-i)
        return t