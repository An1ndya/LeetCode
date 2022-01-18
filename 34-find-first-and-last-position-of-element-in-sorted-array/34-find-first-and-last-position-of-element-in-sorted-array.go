func searchRange(nums []int, target int) []int {
    
    result := []int{-1,-1}
    n:=len(nums)
    l:=0 
    r:=n-1
    
    //if nums[l] == target && nums[r] == target {return []int{l,r}}

    for l <= r {
        m:= int((l+r)/2)
        if nums[m] == target{
            left:= m
            right:=m
            
            for right < n {
                if nums[right] != target {break}
                right++
            }
            for  left > -1 {
                if nums[left] != target {break}
                left--
            }
                
            return []int{left+1,right-1}
                           
        }
        if nums[m] > target{
            r = m - 1
        }else{
            l = m + 1
        }
    }
    return result
    
}