use std::cmp;
impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> 
    {
        let n = intervals.len();
        let mut vec = intervals.clone();
        vec.sort_by(|a, b| a[0].partial_cmp(&b[0]).unwrap());
        let mut ans = vec![];
        ans.push(vec[0].clone());
        for i in 1..n
        {
            let mut a = ans.pop().unwrap();
            let mut b = vec[i].clone();
            if(a[1]>=b[0])
            {
                //overlapped
                ans.push(vec![a[0], cmp::max(a[1],b[1])]);
            }
            else{
                ans.push(a);
                ans.push(b);
            }
            
        }
        return ans;
    }
}