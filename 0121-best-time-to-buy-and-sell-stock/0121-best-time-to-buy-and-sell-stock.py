class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = 100000
        maxprofit=0
        n=len(prices)
        for i in range(0,n,1):
            if minval > prices[i]:
                minval= prices[i]
            else:
                maxprofit=max(maxprofit,prices[i]-minval)
        return maxprofit
        