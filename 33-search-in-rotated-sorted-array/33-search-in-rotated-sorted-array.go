func search(nums []int, target int) int {
    result := -1
    n:=len(nums)
    l:=0 
    r:=n-1
    
    for l <= r {
        //fmt.Println(l, " ",r)
        m:= int((l+r)/2)
        
        if nums[m] == target{ return m }
        
        if nums[r] == target { return r}
        
        if nums[l] < nums[m] {
            if target < nums[m] && target >= nums[l]{
                r = m - 1 
            }else{
                l = m + 1
            }
        }else{
            if target > nums[m] && target <= nums[r]{
                l = m + 1 
            }else{
                r = m - 1
            }
        }
    }
    return result
}