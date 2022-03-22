impl Solution {
    pub fn is_monotonic(nums: Vec<i32>) -> bool 
    {
        let n = nums.len();
        if(n==1){return true;}
        let mut i = 1usize;
        //skip monotone
        while(i<n && nums[i-1]==nums[i]){i+=1;}
        if(i==n){return true;}
        
        let isIncreasing = nums[i-1]<nums[i];
        
        for j in i+1..n
        {
            if(isIncreasing)
            {
                if(nums[j-1]>nums[j]){return false;}
            }else{
                if(nums[j-1]<nums[j]){return false;}
            }
        }
        return true;
    }
}