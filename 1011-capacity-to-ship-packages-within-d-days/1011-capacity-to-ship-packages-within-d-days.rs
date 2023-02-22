use std::cmp;
impl Solution {
    pub fn ship_within_days(weights: Vec<i32>, days: i32) -> i32 {
        let n = weights.len();
        let mut high = 0;
        let mut low  = 0;
        for i in 0..n
        {
            low=cmp::max(low, weights[i]);
            high+=weights[i];
        }
        while(low < high)
        {
            let mut mid = (low+high)/2;
            //println!("{}", mid);
            let mut curcapacity =0;
            let mut daycount =1;
            for i in 0..n
            {
                curcapacity+=weights[i];
                if(curcapacity>mid)
                {
                    curcapacity=weights[i];
                    daycount+=1;
                }
            }
            if(daycount > days)
            {
                low=mid+1;
            }else{
                high=mid;
            }
        }
        return low;
    }
}