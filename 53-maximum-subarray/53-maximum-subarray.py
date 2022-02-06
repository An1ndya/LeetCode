class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sm=0
        mx=-100000
        n=len(nums)
        for i in nums:
            sm+=i
            if sm>mx: mx=sm
            if sm<0: sm=0    
        return mx
        