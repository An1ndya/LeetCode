impl Solution {
    pub fn count_orders(n: i32) -> i32 
    {
        let k = n as usize;
        let mut dp = vec![0i64; k+1];
        dp[1]=1;
        let mut numofnewcombination=1; //number of new possible way if adding i th pairs
        let mut previpaircountplusone =1;
        for i in 2..k+1
        {
            //adding previpaircountplusone+1 and previpaircountplusone+2
            numofnewcombination+=2*(previpaircountplusone) + 3;
            previpaircountplusone+=2;
            dp[i]=(numofnewcombination*dp[i-1])%1000000007;
            //println!("{}", numofnewcombination);
        }
        return dp[k] as i32;
    }
}