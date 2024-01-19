use std::cmp;
impl Solution {
    pub fn min_falling_path_sum(matrix: Vec<Vec<i32>>) -> i32 
    {
        let n = matrix.len();
        let mut dp = matrix.clone();
        let dir:[i32;2] = [-1,1];
        let mut col=0;
        let mut min=1000000000;
        for i in 1..n
        {
            for j in 0..n
            {
                //setting cost from exact upper row
                dp[i][j]+=dp[i-1][j];
                for k in 0..2
                {
                    col=(j as i32 + dir[k]) as usize;
                    if(col>=0 && col<n)
                    {
                        //check if left and right column of upper row
                        //if minimum cost come from any of them update
                        dp[i][j]=cmp::min(dp[i-1][col]+matrix[i][j],dp[i][j]);
                    }
                }
            } 
        }
        for j in 0..n
        {
            //take minimum cost of each column of last row's path
            min=cmp::min(min,dp[n-1][j]);
        }
        
        return min;
    }
}