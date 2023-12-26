class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp=[[0 for i in range(n+1)] for j in range(target+1)]
        dp[0][0]=1
        
        for t in range(1,target+1):
            for dice in range(1,n+1):
                for value in range(1,k+1):
                    #print(t-value)
                    if t<value: break
                    dp[t][dice]+=dp[t-value][dice-1]
                    dp[t][dice]%=1000000007
        return dp[target][n]
            