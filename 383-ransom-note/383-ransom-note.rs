impl Solution {
    pub fn can_construct(ransom_note: String, magazine: String) -> bool {
        let mut arr1:[i32;26] = [0;26];
        let mut arr2:[i32;26] = [0;26];
        //print!("{}",i);
        for c in ransom_note.chars() {
            let  i = c as i32 - 'a' as i32;
            arr1[i as usize]+=1;
        }
        for c in magazine.chars() {
            let  i = c as i32 - 'a' as i32;
            arr2[i as usize]+=1;
        }
        for i in 0..26{
            if arr1[i] > arr2[i] {
                return false
            }
        }
        return true
    }
}