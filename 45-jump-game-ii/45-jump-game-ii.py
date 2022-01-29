class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        dp[n-1] = 0
        for i in range(n-2,-1,-1):
            mx=i+nums[i]
            if mx > n-1:
                dp[i]=1
            else:
                for j in range(mx,i,-1):
                    if dp[j] !=-1:
                        mn=dp[j]+1
                        if dp[i]==-1 or mn<dp[i]:
                            dp[i]=mn
                    if dp[i]!=-1 and dp[i]==2:
                        break   
        return dp[0]       