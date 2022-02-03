class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        mx=0
        dp=[[0]*(n+1) for i in range(m+1)] #[[0]*n]*m return currpoted array

        for i in range(0,m+1,1):
            for j in range(0,n+1,1):
                if i ==0 or j==0: dp[i][j] = 0
                else:
                    if text1[i-1]==text2[j-1]:
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j] = max(dp[i-1][j],dp[i][j-1])    
        return dp[m][n]