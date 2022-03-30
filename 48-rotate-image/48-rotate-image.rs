impl Solution {
    pub fn rotate(matrix: &mut Vec<Vec<i32>>) 
    {
        let n = matrix.len();
        Solution::transpose(matrix);
        Solution::mirror(matrix);
    }
    pub fn transpose(matrix: &mut Vec<Vec<i32>>) 
    {
        let n = matrix.len();
        for i in 0..n
        {
            for j in 0..i
            {
                let temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }
    pub fn mirror(matrix: &mut Vec<Vec<i32>>) 
    {
        let n = matrix.len();
        for i in 0..n
        {
            for j in 0..n/2
            {
                let temp = matrix[i][j];
                matrix[i][j] = matrix[i][n-1-j];
                matrix[i][n-1-j] = temp;
            }
        }
    }
}