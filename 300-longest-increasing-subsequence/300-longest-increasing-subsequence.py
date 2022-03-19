class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        mx=1
        dp=[1]*n #max subsequence at this position
        for i in range(0,n,1):
            for j in range(0,i,1):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
                    if dp[i]>mx: mx=dp[i]               
        return mx