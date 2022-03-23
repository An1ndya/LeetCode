impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> 
    {
        let n=digits.len();
        let mut ans = vec![];
        let mut add=1;
        for i in 1..n+1
        {
            add+=digits[n-i];
            if(add>9)
            {
                ans.push(0);
                add=1;
            }else{
                ans.push(add);
                add=0;
            }
        }
        if(add>0){ans.push(add);}
        
        return ans.into_iter().rev().collect();
    }
}