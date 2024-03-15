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
                //product of all element
                p=p*nums[i];   
            }
        }
        if(zero>1)
        {
            //multiple zero, so all elements will become zero
            return ans;
        }
        else if(zero==1)
        {
            //if one zero position only that position have multiplied p
            ans[zeroi]=p;
            return ans;
        }
        for i in 0..n
        {
            //total multiplied value divided by current position
            ans[i]=p/nums[i];
        }
        return ans;
    }
}