class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=0
        mx=0
        for p in range(n):
            if nums[p]>mx:
                mx=nums[p]
                i=p
        mx=0
        for p in range(n):
            if nums[p]>mx and p!=i:
                mx=nums[p]
                j=p
        return (nums[i]-1)*(nums[j]-1)