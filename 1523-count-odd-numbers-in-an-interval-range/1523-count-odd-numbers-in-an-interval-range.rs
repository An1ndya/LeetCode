impl Solution {
    pub fn count_odds(low: i32, high: i32) -> i32 
    {
        let mut ans = 0;
        let mut range = high - low + 1;
        if( range % 2 == 0 )
        {
              ans = range/2;
        }
        else
        {
            if(low % 2 ==0)
            {
                ans = range/2;
            }
            else
            {
                ans = range/2+1;
            }
        }
        return ans;
    }
}