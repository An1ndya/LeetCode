use std::cmp;
impl Solution {
    pub fn maximal_square(matrix: Vec<Vec<char>>) -> i32 
    {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut dp = vec![vec![0;n+1];m+1]; //length of one side of squre
        let mut mxlen = 0;
        for i in 1..m+1
        {
            for j in 1..n+1
            {
                if(matrix[i-1][j-1]=='1')
                {
                    dp[i][j] = cmp::min(dp[i-1][j-1], cmp::min(dp[i-1][j], dp[i][j-1]))+1;
                    if(dp[i][j] > mxlen) {mxlen = dp[i][j];}
                }
            }
        }
        return mxlen*mxlen;
    }
}