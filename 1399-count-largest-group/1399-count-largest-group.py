from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        digit_sum_count = defaultdict(int)
        
        for num in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(num))
            digit_sum_count[digit_sum] += 1
        
        max_size = max(digit_sum_count.values())
        
        return sum(1 for count in digit_sum_count.values() if count == max_size)

