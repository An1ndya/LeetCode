class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n<d: return -1
        
        @lru_cache(None)
        def dfs(curindex,dayleft):
            if dayleft == 1 : 
                return max(jobDifficulty[curindex:])
            ans, maxd = 10000000000,0
            
            for i in range(curindex, n-dayleft+1):
                maxd=max(maxd,jobDifficulty[i])
                ans= min(ans, maxd + dfs(i+1, dayleft-1))
            return ans
        return dfs(0,d)
                
            