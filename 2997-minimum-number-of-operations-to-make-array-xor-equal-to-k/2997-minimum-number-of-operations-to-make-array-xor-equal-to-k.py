class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for num in nums:
            xor = xor ^ num
        count = 0
        while xor!=k :
            if xor & 1 != k & 1:
                count += 1
            xor = xor >> 1
            k = k >> 1
        return count