impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut arr:[i32;26] = [-1;26];
        let mut minindex=-1;

        for (i, c) in s.chars().enumerate() {
            let  k = c as i32 - 'a' as i32;
            
            if arr[k as usize]==-1{
                arr[k as usize] = i as i32;
            }else{
                arr[k as usize]=-2;
            }
        }
        for i in 0..26{
            if arr[i]>-1{
                if minindex ==-1{
                    minindex=arr[i];
                }else{
                    if arr[i]<minindex{
                        minindex=arr[i];
                    }
                }
            }
        }
        return minindex
        //print!("{}",i);
    }
}