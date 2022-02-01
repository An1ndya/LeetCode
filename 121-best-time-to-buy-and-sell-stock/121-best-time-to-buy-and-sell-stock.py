class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=-1
        minval = 100000
        maxi=-1
        maxval = 0
        profit = 0
        maxprofit=0
        n=len(prices)
        for i in range(0,n,1):
            if maxval < prices[i]:
                maxval=prices[i]
                maxi=i
            if mini != -1 and maxi!=-1 and mini<maxi:
                profit=maxval-minval
                if profit> maxprofit:
                    maxprofit=profit

            if minval > prices[i]:            
                minval=prices[i]
                mini=i
                maxi=-1 
                maxval = 0
        return maxprofit
        