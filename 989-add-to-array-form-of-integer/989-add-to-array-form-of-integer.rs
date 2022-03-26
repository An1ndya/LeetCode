impl Solution {
    pub fn add_to_array_form(num: Vec<i32>, k: i32) -> Vec<i32> 
    {
        let n=num.len();
        let mut ans = vec![];
        let mut add=k;
        for i in 1..n+1
        {
            add+=num[n-i];
            if(add>9)
            {
                ans.push(add%10);
                add/=10;
            }else{
                ans.push(add);
                add=0;
            }
        }
        while(add>0)
        {
            ans.push(add%10);
            add/=10;
        }
        
        return ans.into_iter().rev().collect();     
    }
}