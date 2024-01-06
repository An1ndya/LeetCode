class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
                
        def nextjobprofit(cur):       
            l = cur + 1;
            h = n -1;
            while  l <= h :
                m = l + (h - l)//2;
                if jobs[m][0] >= jobs[cur][1]:
                    h = m-1
                else:
                    l = m + 1;

            return dp[l]
        
        n=len(startTime)
        mx=0
        jobs = sorted(zip(startTime,endTime,profit ))
        dp=[0]*(n+1)
        dp[n-1] = jobs[n-1][2]
        for curjob in range(n-1,-1,-1):
            #include curjob profit
            include_profit = jobs[curjob][2] + nextjobprofit(curjob)
            exclude_profit = dp[curjob+1]
            dp[curjob] = max(include_profit,exclude_profit)
        return dp[0]
