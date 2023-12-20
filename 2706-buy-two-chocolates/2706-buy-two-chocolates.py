class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        mn1=101
        mn2=101
        for i in range(len(prices)):
            if prices[i]<mn1:
                mn2=mn1
                mn1=prices[i]            
            else:
                mn2=min(mn2,prices[i])
        #print(mn1,mn2)
        if money>=mn1+mn2:
            return money-mn1-mn2
        else:
            return money