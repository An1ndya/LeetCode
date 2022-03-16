use std::cmp;
impl Solution {
    pub fn matrix_block_sum(mat: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> 
    {
        let m = mat.len();
        let n = mat[0].len();
        let mut sum = vec![vec![0; n+1]; m+1]; //extra space to remove uncesseay negative index check
                                                // rectangular sum from 0,0 to i,j
        for i in 1..m+1
        {
            for j in 1..n+1
            {
                sum[i][j]=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+mat[i-1][j-1];
            }   
        }
        let mut dp = vec![vec![0; n]; m];   //our desired answer
        let p= k as usize;
        for i in 0..m
        {
            for j in 0..n
            {
                let mut r1 = if(i>p){i-p}else{0} ;
                let mut c1 = if(j>p){j-p}else{0} ;
                let mut r2 = cmp::min(i+1+p,m);
                let mut c2 = cmp::min(j+1+p,n);
                //println!("{}",r1);
                dp[i][j]=sum[r2][c2]-sum[r2][c1]-sum[r1][c2]+sum[r1][c1];
            }   
        }
        return dp;
    }
}