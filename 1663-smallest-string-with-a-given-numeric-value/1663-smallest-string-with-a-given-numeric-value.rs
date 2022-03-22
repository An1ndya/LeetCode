impl Solution {
    pub fn get_smallest_string(n: i32, k: i32) -> String 
    {
        let mut len = n;
        let mut sum = k;
        let mut str = String::new();
        while(len>0)
        {
            let mut val = sum-(len-1); 
            if(val>26)
            {
                sum-=26;
                str.push('z');
            }else{
                sum-=val;
                let mut c = ('a' as u8 + (val-1) as u8) as char;
                str.push(c);
            }
            len-=1;
        }
        //println!("{:?}",str);
        return str.chars().rev().collect();
    }
}