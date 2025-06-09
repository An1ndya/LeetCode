class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        pos = 0
        ans = 0
        def dfs(curr):
            nonlocal pos, ans

            if curr > n:
                return
            pos += 1
            if pos == k:
                ans = curr
                return 
            for i in range(10):
                next_num = curr * 10 + i
                dfs(next_num)
        
        for i in range(1, 10):
            if ans != 0:
                return ans
            dfs(i)
        
        return ans