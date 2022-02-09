class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        k=len(original)
        if m*n!=k: return []
        ans=[[0]*n for i in range(m)]
        p=0
        for i in range(m):
            for j in range(n):
                ans[i][j]=original[p]
                p+=1
        return ans        