class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for j in range(i,n): 
                    if s[i:j+1] in wordDict:
                        dp[j+1]= True
                        
        return dp[n]  
    
    
