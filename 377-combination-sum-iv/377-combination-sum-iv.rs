impl Solution {
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 
    {
        let mut dp = vec![0;(target+1)as usize];
        dp[0]=1;
        for i in 1..(target+1)as usize 
        {
            for c in nums.iter() 
            {            
                if(i>=*c as usize){ dp[i]+=dp[i-*c as usize];}
            }
        }
        return dp[target as usize];
        
    }
}