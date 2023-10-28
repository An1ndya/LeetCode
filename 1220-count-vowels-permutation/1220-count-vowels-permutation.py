class Solution:
    def countVowelPermutation(self, n: int) -> int:
               
        dp=[[0 for v in range(n)] for i in range(5)]
        
        for v in range(5):
            dp[v][0]=1
        for i in range(1,n):
            for v in range(5):
                match v:
                    case 0:
                        #e,i,u->a
                        dp[0][i]=dp[1][i-1]+dp[2][i-1]+dp[4][i-1]
                    case 1:
                        #a,i->e
                        dp[1][i]=dp[0][i-1]+dp[2][i-1]
                    case 2:
                        #e,o->i
                        dp[2][i]=dp[1][i-1]+dp[3][i-1]
                    case 3:
                        #i->o
                        dp[3][i]=dp[2][i-1]
                    case 4:
                        #i,o->u
                        dp[4][i]=dp[2][i-1]+dp[3][i-1]
                dp[v][i]%=1000000007
        ans=0
        
        for v in range(5): 
            #print(dp[v][n-1])
            ans+= dp[v][n-1]
            ans%=1000000007
            
        return ans