class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_length = 1
        inc = dec = 1  # Track increasing and decreasing sequences

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Increasing sequence
                inc += 1
                dec = 1  # Reset decreasing sequence
            elif nums[i] < nums[i - 1]:  # Decreasing sequence
                dec += 1
                inc = 1  # Reset increasing sequence
            else:
                inc = dec = 1  # Reset both if elements are equal
            
            max_length = max(max_length, inc, dec)
        
        return max_length 