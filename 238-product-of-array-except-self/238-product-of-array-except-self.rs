impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> 
    {
        let n = nums.len();
        let mut p =1;
        let mut zero = 0;
        let mut zeroi = 0usize;
        let mut ans = vec![0;n];
        
        for i in 0..n
        {
            if(nums[i]==0)
            {
                zero+=1;
                zeroi = i;
            }else
            {
                p=p*nums[i];   
            }
        }
        if(zero>1)
        {
            return ans;
        }
        else if(zero==1)
        {
            ans[zeroi]=p;
            return ans;
        }
        for i in 0..n
        {
            ans[i]=p/nums[i];
        }
        return ans;
    }
}