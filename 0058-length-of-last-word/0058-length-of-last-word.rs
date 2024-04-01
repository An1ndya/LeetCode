impl Solution {
    pub fn length_of_last_word(s: String) -> i32 
    {
        let n = s.len();
        let mut lastspace = -1;
        let mut ans = 0;
        for (i, c) in s.chars().enumerate() 
        {
            if(c==' ')
            {               
                lastspace=i as i32;
            }
            else
            {
                ans = i as i32 -lastspace;
            } 
        }
        return ans;
    }
}