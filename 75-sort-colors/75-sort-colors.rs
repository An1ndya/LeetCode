impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) 
    {
        let n = nums.len();
        let mut zero = 0usize;    
        let mut one = 0usize;  
        let mut two = 0usize; 
        for i in 0..n
        {
            if(nums[i]==0){zero+=1;}
            else if(nums[i]==1){one+=1;}
            else if(nums[i]==2){two+=1;}
        }
        for i in 0..zero                    {nums[i]=0;}
        for i in zero..zero+one             {nums[i]=1;}
        for i in zero+one..zero+one+two     {nums[i]=2;}
    }
}