class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]  # Extend the ascending subarray
            else:
                max_sum = max(max_sum, current_sum)  # Update max_sum
                current_sum = nums[i]  # Start a new subarray
        
        return max(max_sum, current_sum) 