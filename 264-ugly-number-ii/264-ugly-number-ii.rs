use std::cmp;
impl Solution {
    pub fn nth_ugly_number(n: i32) -> i32 {
        let p = n as usize;
        let mut arr = vec![Default::default(); p];
        arr[0]=1;
        let mut m2=0;
        let mut m3=0;
        let mut m5=0;
        for i in 1..p
        {
            arr[i]=cmp::min(2*arr[m2],cmp::min(3*arr[m3],5*arr[m5]));
            
            if(arr[i]==2*arr[m2]){m2+=1;}
            if(arr[i]==3*arr[m3]){m3+=1;}
            if(arr[i]==5*arr[m5]){m5+=1;}
        }
        return arr[p-1];
    }
}