use std::cmp;
impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let n = height.len();
        let mut trap = 0;
        //array for ith position and both its left and right side possible maximum height
        //use this to calculate water level
        let mut maxleftheight = vec![Default::default(); n];
        let mut maxrightheight = vec![Default::default(); n];
        // left and right position water height should be 0, as no wall there
        maxleftheight[0] = 0;
        maxrightheight[n-1] = 0;
        for i in 1..n {
            //from left 0 to i-1
            maxleftheight[i]     = cmp::max(maxleftheight[i-1],height[i-1]);
            //from right n-1 to n-i
            maxrightheight[n-1-i]= cmp::max(maxrightheight[n-i],height[n-i]);
        }
        for i in 1..n-1{
            //water lever at ith = min(maxleftheight[i],maxrightheight[i])
            //ith position trap water = min(maxleftheight[i],maxrightheight[i])-height[i]
            trap += cmp::max(0,cmp::min(maxleftheight[i],maxrightheight[i])-height[i]);
        }       
        return trap;
    }
}