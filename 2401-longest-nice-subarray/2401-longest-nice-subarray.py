class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        currAND = 0
        max_len = 0
        
        for right in range(len(nums)):
            while (currAND & nums[right]) != 0:
                currAND ^= nums[left]  # Remove nums[left] from the window
                left += 1
            
            currAND |= nums[right]  # Add nums[right] to the window
            max_len = max(max_len, right - left + 1)  # Update max length
        
        return max_len