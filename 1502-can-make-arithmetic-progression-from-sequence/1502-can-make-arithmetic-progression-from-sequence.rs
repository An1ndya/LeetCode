impl Solution {
    pub fn can_make_arithmetic_progression(arr: Vec<i32>) -> bool 
    {
        let mut nums = arr.clone();
        nums.sort();
        let d=nums[1]-nums[0];
        for i in 2..nums.len()
        {
            if(d!=nums[i]-nums[i-1])
            {
                return false;
            }
        }
        return true;
    }
}