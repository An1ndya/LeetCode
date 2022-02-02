class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        mx=1
        l=1
        n=len(nums)
        for i in range(1,n,1):
            if nums[i]>nums[i-1]:
                l+=1
                if l>mx: mx=l
            else:
                l=1
        return mx