impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 
    {
        
        let m = obstacle_grid.len();
        let n = obstacle_grid[0].len();
        let mut dp = vec![vec![0; n]; m]; //number of ways to reach i, j from 0,0
        dp[0][0]=1; 
        for i in 0..m
        {
            for j in 0..n
            {
                if(obstacle_grid[i][j]!=1)
                {
                    //dp[i][j]=dp[i-1][j]+dp[i][j-1];
                    if(i>0){ dp[i][j]+=dp[i-1][j];}
                    if(j>0){ dp[i][j]+=dp[i][j-1];}
                }else
                {
                    dp[i][j]=0; 
                }
            }   
        }
        return dp[m-1][n-1];
    }
}