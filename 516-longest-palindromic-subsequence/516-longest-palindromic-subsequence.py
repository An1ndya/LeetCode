class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # same concept as https://leetcode.com/problems/longest-common-subsequence/
        r = s[::-1] #reverse the string
        m,n=len(s),len(r)
        mx=1
        dp=[[0]*(n+1) for i in range(m+1)] #[[0]*n]*m return currpoted array

        for i in range(1,m+1,1):
            for j in range(1,n+1,1):
                if s[i-1]==r[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])    
        return dp[m][n]