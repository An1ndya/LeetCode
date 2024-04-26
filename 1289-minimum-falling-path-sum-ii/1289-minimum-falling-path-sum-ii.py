class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = grid
        for i in range(1,n):
            for j in range(m):
                minpath = 1000000000
                for k in range(m):
                    if k !=j:
                        minpath = min(minpath,dp[i-1][k])
                dp[i][j] += minpath
        minpathsum = 10000000000
        for j in range(m):
            minpathsum = min(minpathsum,dp[n-1][j])
        return minpathsum