impl Solution {
    pub fn maximum_wealth(accounts: Vec<Vec<i32>>) -> i32 
    {
        let m=accounts.len();
        let n=accounts[0].len();
        let mut mx=0;
        for i in 0..m
        {
            let mut wealth =0;
            for j in 0..n
            {
                wealth+=accounts[i][j];
            }
            if(wealth>mx){mx=wealth;}
        }
        return mx;
    }
}