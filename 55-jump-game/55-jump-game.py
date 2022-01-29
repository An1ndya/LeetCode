class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        mxindex=0
        i=0
        while i <=mxindex:
            if nums[i]+i > mxindex : mxindex = nums[i]+i
            if mxindex >= n-1: return True
            i+=1
        return False
    
                