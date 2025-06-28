class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair each number with its index
        indexed_nums = list(enumerate(nums))
        
        # Sort based on value descending, take top k
        top_k = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]
        
        # Sort those k elements based on their original index to preserve order
        top_k_sorted = sorted(top_k, key=lambda x: x[0])
        
        # Extract the values to return
        return [num for idx, num in top_k_sorted]
