use std::cmp;
impl Solution {
    pub fn max_profit(prices: Vec<i32>, fee: i32) -> i32 
    {
        let mut cash=0;
        let mut cashwithstock=-prices[0];
        
        for price in prices
        {
            cash = cmp::max(cash, cashwithstock+price-fee);
            cashwithstock = cmp::max(cashwithstock,cash-price);
        }
        return cash;
    }
}