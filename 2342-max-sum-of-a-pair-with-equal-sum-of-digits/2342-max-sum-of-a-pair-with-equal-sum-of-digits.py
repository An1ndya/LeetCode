class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(n))
        
        digit_map = defaultdict(list)
        
        # Group numbers by digit sum
        for num in nums:
            s = digit_sum(num)
            digit_map[s].append(num)
        
        max_sum = -1
        
        # Check each group
        for key in digit_map:
            if len(digit_map[key]) > 1:
                # Get two largest numbers in this group
                largest_two = sorted(digit_map[key], reverse=True)[:2]
                max_sum = max(max_sum, sum(largest_two))
        
        return max_sum