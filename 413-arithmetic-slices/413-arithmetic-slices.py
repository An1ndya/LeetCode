class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        i=2
        ans=0
        c=0
        while i<n:
            if nums[i-2]-nums[i-1]==nums[i-1]-nums[i]:
                c+=1
                ans+=c
            else:
                c=0
            i+=1
        return ans
            