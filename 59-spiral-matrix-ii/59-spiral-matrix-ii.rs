impl Solution {
    pub fn generate_matrix(n: i32) -> Vec<Vec<i32>>
    {
        let k = n as usize;
        let mut count =0;    
        let mut ans = vec![vec![0;k];k];
        let dir: Vec<[i32;2]> = vec![[0,1],[1,0],[0,-1],[-1,0]];
        let mut dirIndex = 0usize;
        let mut row =0;
        let mut col =0;
        while(count < n*n)
        {
            count+=1;
            ans[row as usize][col as usize] = count;
            let mut r = row + dir[dirIndex][0];
            let mut c = col + dir[dirIndex][1];
            
            if(r>n-1 || c>n-1 || r<0 || c<0 || ans[r as usize][c as usize]!=0)
            {
                dirIndex = (dirIndex+1) % 4;
            }
            
            row+= dir[dirIndex][0];
            col+= dir[dirIndex][1];
        }
        
        return ans;
    }
}