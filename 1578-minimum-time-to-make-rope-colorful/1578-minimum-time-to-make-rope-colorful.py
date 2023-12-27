class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        dp=[0]*n
        ans=0
        time=neededTime[0]
        mx= time
        c=1
        for i in range(1,n):          
            if colors[i-1]==colors[i]:
                time+=neededTime[i]
                mx = max(mx,neededTime[i])
                c+=1
            else:
                ans+=time-mx
                time=neededTime[i]
                mx=neededTime[i]
                c=1
        if c>1:
            ans+=time-mx
        return ans