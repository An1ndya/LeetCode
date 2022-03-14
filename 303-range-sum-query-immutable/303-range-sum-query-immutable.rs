struct NumArray {
    prefixsum: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {

    fn new(nums: Vec<i32>) -> Self {
        let mut sum=0;
        let mut prefixsum= Vec::new();
        for n in nums
        {
            sum+=n;
            prefixsum.push(sum);
        }
        return NumArray{prefixsum};
    }
    
    fn sum_range(&self, left: i32, right: i32) -> i32 {
        if(left>0)
        {
            return self.prefixsum[right as usize]-self.prefixsum[(left-1) as usize];
        }else{
            return self.prefixsum[right as usize];
        }
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * let ret_1: i32 = obj.sum_range(left, right);
 */