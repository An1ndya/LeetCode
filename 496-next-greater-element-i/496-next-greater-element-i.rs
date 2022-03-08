use std::collections::HashMap;
impl Solution {
    pub fn next_greater_element(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> 
    {
        let n= nums2.len();
        let mut map: HashMap<i32, i32> = HashMap::new();
        let mut stack: Vec<i32> = Vec::new();
        let mut ans: Vec<i32> = Vec::new();
        let mut last: usize=0;
        
        
        
        for n in nums2
        {
            while(last>0 && stack[last-1]<n)
            {
                map.insert(stack.pop().unwrap(),n);
                last-=1;
            }
            stack.push(n);
            last+=1;
        }
        for n in nums1
        {
            if( map.contains_key(&n) )
            {
                ans.push(*map.get(&n).unwrap());
            }else
            {
                ans.push(-1);
            }
        }
        return ans;
    }
}