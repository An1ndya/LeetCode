class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for i in range(k+1)] for j in range(n+1)]
        #following initiliaze is highly important
        #as K>=N will use this subtraction during dp[1][1]
        #not setting this will result in dp[1][1]=1, but it should be 1
        dp[0][0]=1
        
        #relation betwen subproblems
        #f(n,k) = f(n-1,k)+f(n-1,k-1)+f(n-1,k-2)+....f(n-1,0)
        #n th value in array can create 0,1,2,3...,n-1 new inverse pair
        #by placing from last sequentially
        #so sum all arrangements of previous value of inverse pair
        #use dp to store
        '''
        for N in range(1,n+1):
            for K in range(k+1):
                for i in range(0,min(K,N-1)+1):
                    dp[N][K]+= dp[N-1][K-i] 
                    dp[N][K] %= 1000000007
        '''
        #upper approach return 10^9 complexity for n=1000, k=1000
        #optimization 
        #sliding window
        for N in range(1,n+1):
            for K in range(k+1):
                if K==0: 
                    dp[N][K] = 1
                    continue
                #previous N, K just like sliding window
                dp[N][K] = dp[N-1][K] + dp[N][K-1]  

                dp[N][K] %= 1000000007
                # K index should be no more than 0
                # so extra added value should be subtracted
                if (K >= N):
                    dp[N][K] -= dp[N - 1][K - N] 
                dp[N][K] %= 1000000007
        return dp[n][k]