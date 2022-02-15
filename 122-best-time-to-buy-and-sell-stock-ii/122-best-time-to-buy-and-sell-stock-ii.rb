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
        else
            if prices[i]-minval > maxprofit; maxprofit = prices[i]-minval end
        end
        if i+1<n and prices[i+1]> prices[i];
            dailyprofit += prices[i+1]-prices[i]
            if dailyprofit > maxprofit; maxprofit = dailyprofit end
        end
    end
    return maxprofit  
end