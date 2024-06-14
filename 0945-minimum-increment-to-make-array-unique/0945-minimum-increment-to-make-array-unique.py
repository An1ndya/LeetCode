class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        move = 0
        for i in range(1,n):
            if nums[i-1] >= nums[i]:
                #required move to set nums[i] = nums[i-1]+1
                move += nums[i-1] - nums[i] + 1
                #increase current digit to previous + 1
                nums[i] = nums[i-1] + 1
        return move