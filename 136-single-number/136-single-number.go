func singleNumber(nums []int) int {
    singleone := 0 
    m:= make(map[int]bool)
    for i:=0;i<len(nums);i++{
        if m[nums[i]]{
            delete(m, nums[i])
            singleone = singleone - nums[i]
        }else{
            m[nums[i]] = true
            singleone = singleone + nums[i] 
        }
    }
    return singleone
}