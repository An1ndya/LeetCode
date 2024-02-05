impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut arr:[i32;26] = [-1;26];
        let mut minindex=-1;

        for (i, c) in s.chars().enumerate() {
            let  k = c as i32 - 'a' as i32;
            
            if arr[k as usize]==-1{
                //if first occurance update index
                arr[k as usize] = i as i32;
            }else{
                //if not first occurance set -2 or negative
                arr[k as usize]=-2;
            }
        }
        for i in 0..26{
            if arr[i]>-1{
                if minindex ==-1{
                    //minindex not updated before
                    minindex=arr[i];
                }else{
                    //update minindex to previous unique occurance index
                    if arr[i]<minindex{
                        minindex=arr[i];
                    }
                }
            }
        }
        return minindex
    }
}