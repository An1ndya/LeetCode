import heapq
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        total_len = 3 * n

        # left[i]: minimum sum of n elements from nums[0..i]
        max_heap = []
        left_sum = 0
        left = [0] * total_len

        for i in range(2 * n):
            heapq.heappush(max_heap, -nums[i])  # Use negative for max-heap
            left_sum += nums[i]
            if len(max_heap) > n:
                left_sum += heapq.heappop(max_heap)
            if len(max_heap) == n:
                left[i] = left_sum
            else:
                left[i] = float('inf')

        # right[i]: maximum sum of n elements from nums[i..]
        min_heap = []
        right_sum = 0
        right = [0] * total_len

        for i in range(total_len - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])  # Min-heap
            right_sum += nums[i]
            if len(min_heap) > n:
                right_sum -= heapq.heappop(min_heap)
            if len(min_heap) == n:
                right[i] = right_sum
            else:
                right[i] = float('-inf')

        # Compute min difference
        result = float('inf')
        for i in range(n - 1, 2 * n):
            if left[i] != float('inf') and right[i + 1] != float('-inf'):
                result = min(result, left[i] - right[i + 1])

        return result
