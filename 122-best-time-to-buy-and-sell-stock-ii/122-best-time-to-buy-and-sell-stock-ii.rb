# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    minval = 100000
    maxprofit=0
    dailyprofit =0
    n=prices.length()
    for i in 0..n-1
        if minval > prices[i]
            minval= prices[i]
        elsif prices[i]> minval
            maxprofit += prices[i]-minval 
            minval= prices[i]
        end
    end
    return maxprofit  
end