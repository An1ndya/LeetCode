func firstMissingPositive(nums []int) int {
    m:= make(map[int]bool)
    //min:= math.MaxInt64
    for i:=0;i<len(nums);i++{
        m[nums[i]] = true
        //if nums[i] < min {min = nums[i]}
    }
    for i:=1;i<math.MaxInt64;i++{
        if m[i] == false{
            return i
        }
    }  
    return -1
}