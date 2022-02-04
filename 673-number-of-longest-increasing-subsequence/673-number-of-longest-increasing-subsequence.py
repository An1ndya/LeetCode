class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        mx=1
        n=len(nums)
        ans=0
        dp=[1]*n  #length subsequence 
        c= [1]*n  #combination number to that index
        for i in range(0,n,1):
            for j in range(0,i,1):
                if nums[i]>nums[j]:
                    if dp[j]+1 > dp[i]:
                        dp[i]=dp[j]+1
                        c[i] = c[j]
                    elif dp[j]+1==dp[i]:  
                        #this j will add extra combination
                        c[i] += c[j]
            if dp[i]>mx:
                mx=dp[i]
                ans=c[i]
            elif dp[i]==mx:
                ans+=c[i]
        return ans