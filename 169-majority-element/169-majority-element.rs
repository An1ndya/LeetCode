impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 
    {
        let n = nums.len();
        let mut c = 1;
        let mut a = nums;
        a.sort();
        for i in 1..n
        {
            if(a[i]==a[i-1])
            {
                c+=1;
                if(c>n/2){
                    return a[i];
                }
            }
            else
            {
                c=1;
            }
        }
        return a[0];
    }
}