use std::cmp;
impl Solution {
    pub fn min_domino_rotations(tops: Vec<i32>, bottoms: Vec<i32>) -> i32 
    {
        let n = tops.len();
        let mut counttop = vec![0;7];
        let mut countbottom = vec![0;7];
        let mut same = vec![0;7];
        for i in 0..n
        {
            counttop[tops[i] as usize]+=1;
            countbottom[bottoms[i] as usize]+=1;
            if(tops[i]==bottoms[i])
            {
                same[tops[i]as usize]+=1;
            }
        }
        for i in 1..7
        {
            if(counttop[i]+countbottom[i]-same[i]==n as i32)
            {
                return cmp::min(counttop[i],countbottom[i])-same[i];
            }
        }
        return -1;
    }
}