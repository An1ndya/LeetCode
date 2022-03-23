impl Solution {
    pub fn broken_calc(start_value: i32, target: i32) -> i32 
    {
        let mut t = target;
        let mut s = start_value;
        let mut minop =0;
        
        //backward op
        
        while(t>s)
        {
            if(t%2==0)
            {
                t/=2;
            }else
            {
                t+=1;
            }
            minop+=1;
        }
        return minop+s-t;
    }
}