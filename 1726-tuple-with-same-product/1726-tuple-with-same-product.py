class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(list)
        n = len(nums)
        
        # Step 1: Store all pairs and their products
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product].append((nums[i], nums[j]))

        count = 0
        
        # Step 2: Count valid (a, b, c, d) tuples
        for pairs in product_map.values():
            m = len(pairs)
            if m > 1:
                count += (m * (m - 1) // 2) * 8  # C(m,2) * 8

        return count