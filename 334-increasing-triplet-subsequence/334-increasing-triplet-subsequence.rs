impl Solution {
    pub fn increasing_triplet(nums: Vec<i32>) -> bool 
    {
        let n = nums.len();
        let mut seq1 = i32::MAX;
        let mut seq2 = i32::MAX;
        
        for i in 0..n
        {
            if(nums[i]<=seq1)
            {
                seq1 = nums[i];
            }
            else if(nums[i]<=seq2)
            {
                //nums[i] greater than seq1 so it is 2nd increasing number
                seq2 = nums[i];
            }
            else
            {
                //seq3 , so 3rd sequence number found
                return true;
            }
        }
        return false;    
    }
}