func totalHammingDistance(nums []int) int{
    sum := 0

    for i:=0;i<32;i++{
        ones := 0
        zeros := 0
        for j:=0;j<len(nums);j++{
            if nums[j] & 1 == 1{
                ones++    
            }else{
                zeros++
            }
            nums[j] = nums[j] >> 1
        } 
        //only get 1 as result of xor where  elements are 1 and 0 
        //this bit will get as much as the number of combination where elements is 1 and 0 
        //each one can combine with every zero, so total combination ones*zeros  
        sum += ones*zeros
    }
    return sum    
}
