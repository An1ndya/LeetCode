use std::cmp;
impl Solution {
    pub fn num_squares(n: i32) -> i32 
    {
        let mut dp = vec![n;n as usize +1];
        dp[0]=0;
        for i in 0..(n+1) as usize
        {
            let mut j =1usize;
            while(j*j <= n as usize)
            {
                if(i>=j*j)
                {
                    dp[i] = cmp::min(dp[i], dp[i-j*j]+1);
                }
                j+=1;
            }
        }
        return dp[n as usize];
    } 
}