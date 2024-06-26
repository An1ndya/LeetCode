impl Solution {
    pub fn num_rescue_boats(people: Vec<i32>, limit: i32) -> i32 
    {
        let n = people.len();
        let mut arr = people.clone();
        arr.sort();
        let mut l = 0usize;
        let mut r = n -1;
        let mut boat =0;
        while(l<=r)
        {
            if(arr[l]+arr[r]<=limit)
            {   //both maximum and minimum can be arried      
                l+=1;
                r-=1;
            }else{
                //only maximum , not minimum as they canbe carried together with another in next setp
                r-=1;
            }
            boat+=1;
            if(r>n)
            {
                //usize 0-1 return non negative number
                break;
            }
        }
        return boat;    
    }
}