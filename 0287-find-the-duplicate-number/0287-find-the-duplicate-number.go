func findDuplicate(nums []int) int {
    
    m:= make(map[int]bool)
    for i:=0;i<len(nums);i++{
        if m[nums[i]]{
            return nums[i]     
        }else{
            m[nums[i]] = true
        }
    }
    return 0 
}