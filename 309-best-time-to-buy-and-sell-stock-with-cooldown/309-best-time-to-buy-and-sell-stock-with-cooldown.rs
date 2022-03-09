use std::cmp;
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 
    {
        let n = prices.len();
        if( n==1){ return 0;}
        
        let mut buy = vec![0;n];
        let mut sell = vec![0;n];
        //dry run to i=1
        buy[0]=-prices[0];
        sell[0]=0;
        buy[1]= cmp::max(-prices[1], buy[0]);
        sell[1]=cmp::max(buy[0]+prices[1], sell[0]);
        
        for i in 2..n
        {
            //not using rest vector cause rest[i-1]=sell[i-2]
            buy[i] = cmp::max(sell[i-2]-prices[i], buy[i-1]);
            sell[i]= cmp::max(buy[i-1]+prices[i], sell[i-1]);
        }
        return sell[n-1];
    }
}