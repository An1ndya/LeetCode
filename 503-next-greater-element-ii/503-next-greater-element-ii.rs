impl Solution {
    pub fn next_greater_elements(nums: Vec<i32>) -> Vec<i32> 
    {
        let n = nums.len();
        let mut ans = vec![-1;n];
        let mut size= 0usize;
        let mut stack : Vec<usize>= Vec::new();
        
        for i in 0..2*n
        {
            while(size>0 && nums[i%n] > nums[stack[size-1]])
            {
                let index = stack.pop().unwrap();
                size-=1;
                ans[index] = nums[i%n];
            }
            stack.push(i%n);
            size+=1;
        }
        return  ans;    
    }
}