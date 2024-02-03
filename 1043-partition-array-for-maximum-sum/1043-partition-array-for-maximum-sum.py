class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr) 
        dp = [0 for i in range(n+1)] #dp[i] holds answer for length till i
        dp[1] = arr[0]
        
        for i in range(1,n+1):
            maxOfLastJ=0
            for j in range(1,k+1):
                if i-j >=0:
                    maxOfLastJ = max(maxOfLastJ,arr[i-j])
                    # we will check if last k elements max
                    #then dp[i] should be max*k+dp[i-k]
                    #dp[i] can be max sometimes for k=1...to k 
                    #so we will take maximum of k
                    #dp[i-j] + max(A[i-1], ..., A[i-j]) * j 
                    
                    dp[i] = max(dp[i], dp[i-j] + maxOfLastJ *(j))
                else:
                    break
        return dp[n]