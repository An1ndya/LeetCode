class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        mx=0
        dp=[[0]*(n+1) for i in range(m+1)] #[[0]*n]*m return currpoted array

        for i in range(0,m+1,1):
            for j in range(0,n+1,1):
                if i ==0 or j==0: dp[i][j] = 0
                else:
                    if word1[i-1]==word2[j-1]:
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])    
        return m+n-2*dp[m][n]