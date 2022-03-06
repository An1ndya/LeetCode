impl Solution {
    pub fn are_almost_equal(s1: String, s2: String) -> bool {
        let v1 =s1.as_bytes();
        let v2 =s2.as_bytes();
        let n = v1.len();
        let mut c=0;
        let mut index1=0usize;
        let mut index2=0usize;
        for i in 0..n
        {
            if(v1[i]!=v2[i])
            {
                if(c==2){return false;}
                else if(c==0)
                {
                   index1=i;     
                }
                else if(c==1)
                {
                    index2=i; 
                }
                
                c+=1;
            }
        }
        if(c==0){return true;}
        if(c==1){return false;}
        if(c==2 && v1[index1]==v2[index2] && v1[index2]==v2[index1] ){return true;}
        return false;
    }
}