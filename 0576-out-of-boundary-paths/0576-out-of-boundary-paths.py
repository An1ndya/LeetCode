class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        #store path posibble path count to i,j 
        dp = [[0 for j in range(n)] for i in range(m)]
        ans=0
        #update first position with 1
        dp[startRow][startColumn] = 1
        for move in range(1,maxMove+1):
            #to update store path count for current move
            # new list so we dont loss previous move path's count in dp
            temp = [[0 for j in range(n)] for i in range(m)]
            for i in range(m):
                for j in range(n):
                    #if boundary point 
                    #add outgoing path to answer on this move
                    if i ==0 : ans += dp[i][j] 
                    if i ==m-1 : ans += dp[i][j] 
                    if j ==0 : ans += dp[i][j] 
                    if j ==n-1 : ans += dp[i][j] 
                    ans %= 1000000007
                    #update newer path created during this move
                    temp[i][j] = 0
                    temp[i][j] = dp[i-1][j] if i > 0 else 0
                    temp[i][j] += dp[i+1][j] if i <m-1 else 0
                    temp[i][j] += dp[i][j-1] if j > 0 else 0
                    temp[i][j] += dp[i][j+1] if j < n-1 else 0
            #after this move end, update dp result with lastest move
            dp=temp
        return ans