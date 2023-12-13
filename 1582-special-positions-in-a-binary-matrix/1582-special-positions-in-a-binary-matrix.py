class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rowtotal = [0 for i in range(m)]
        coltotal = [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                rowtotal[i]+=mat[i][j]
                coltotal[j]+=mat[i][j]
        #print(rowtotal)
        #print(coltotal)
        ans=0
        for i in range(m):
            for j in range(n):
                if rowtotal[i]==1 and coltotal[j]==1 and mat[i][j]==1:
                    ans+=1
        return ans