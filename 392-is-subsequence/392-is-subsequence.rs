impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool 
    {
        let sn = s.len();
        let tn = t.len();
        let mut si=0;
        let mut ti=0;
        
        while(ti<tn)
        {
            if(si==sn){return true;}
            if(s.as_bytes()[si]==t.as_bytes()[ti])
            {
                ti+=1;
                si+=1;
            }else
            {
                ti+=1;
            }
            
        }
        if(si==sn){return true;}
        else{return false;}
    }
}