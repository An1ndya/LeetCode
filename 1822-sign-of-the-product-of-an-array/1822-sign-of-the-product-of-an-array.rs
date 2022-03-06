impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 
    {
        let mut ans=1;
        for i in nums
        {
            if(i==0){ return 0;}
            else if(i<0){ans*=-1;} 
        }
        return ans;
    }
}