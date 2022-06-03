struct NumMatrix {
    sum: Vec<Vec<i32>>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumMatrix {

    fn new(matrix: Vec<Vec<i32>>) -> Self 
    {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut sum = vec![vec![0; n+1]; m+1]; //extra space to remove uncesseay negative index check
                                                // rectangular sum from 0,0 to i,j
        for i in 1..m+1
        {
            for j in 1..n+1
            {
                sum[i][j]=sum[i-1][j]+sum[i][j-1]-sum[i-1][j-1]+matrix[i-1][j-1];
            }   
        }
        return NumMatrix{sum};
    }
    
    fn sum_region(&self, row1: i32, col1: i32, row2: i32, col2: i32) -> i32 
    {
        let mut r1 = row1 as usize;
        let mut c1 =  col1 as usize ;
        let mut r2 = row2 as usize +1;
        let mut c2 =  col2 as usize +1;
        return self.sum[r2][c2]-self.sum[r2][c1]-self.sum[r1][c2]+self.sum[r1][c1];
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * let obj = NumMatrix::new(matrix);
 * let ret_1: i32 = obj.sum_region(row1, col1, row2, col2);
 */