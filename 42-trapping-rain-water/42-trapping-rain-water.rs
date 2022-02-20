use std::cmp;
impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let n = height.len();
        let mut trap = 0;
        //print!("{}",n);
        let mut lefth = vec![Default::default(); n];
        let mut righth = vec![Default::default(); n];
        lefth[0] = 0;
        righth[n-1] = 0;
        for i in 1..n {
            lefth[i]     = cmp::max(lefth[i-1],height[i-1]);
            righth[n-1-i]= cmp::max(righth[n-i],height[n-i]);
        }
        for i in 1..n-1{
            trap += cmp::max(0,cmp::min(lefth[i],righth[i])-height[i]);
        }    
        //print!("{:?}",lefth);    
        return trap;
    }
}