class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        
        if s[0] == '0': return 0
        if n == 1 : return 1 
        
        dp=[0]*n
        dp[0]= int(s[0]!='0')
        
        if s[1] == '0':
            
            if s[0] > '2': return 0
            dp[1]= dp[0]
        else:  
            if int(s[0:2]) < 27 : dp[1]=2
            else: dp[1]=1
        
        for i in range(2,n,1):
            val = int(s[i-1:i+1])
            if val %10== 0 : 
                if val/10 == 0 or val/10 > 2: return 0
                dp[i]=dp[i-2]
            elif val < 10:
                dp[i]=dp[i-1]
            elif  val < 27:
                dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]
            
        return dp[n-1]