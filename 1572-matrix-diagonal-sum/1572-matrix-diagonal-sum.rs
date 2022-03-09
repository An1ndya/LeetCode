impl Solution {
    pub fn diagonal_sum(mat: Vec<Vec<i32>>) -> i32 
    {
        let n = mat.len();
        let mut sum =0;
        for i in 0..n
        {
            sum+=mat[i][i];
            if(i!=n-1-i){sum+=mat[i][n-1-i];}
        }
        return sum;    
    }
}