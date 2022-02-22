impl Solution {
    pub fn title_to_number(column_title: String) -> i32
    {
        let mut ans = 0;
        let mut mul = 1;
        for (i, c) in column_title.chars().rev().collect::<String>().chars().enumerate() 
        {
            ans+= mul*(c as i32 - 'A' as i32 + 1);
            mul*=26;
        }
        return ans;   
    }
}