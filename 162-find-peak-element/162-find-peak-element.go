func findPeakElement(nums []int) int {
        
    n:=len(nums)
    l:=0 
    r:=n-1
    
    if n == 1 { return 0 }
    
    for l <= r {
        
        //fmt.Println(l, " ",r)
  
        m:= int((l+r)/2)
        
        if m == 0 {
            if nums[m] > nums[m+1] { return m}
        }else if m == n-1{
            if nums[m] > nums[m-1] { return m}
        }else{
            if nums[m] > nums[m-1] && nums[m] > nums[m+1]  { return m}
        }
        
        if nums[m] < nums[m+1] {
            l = m + 1
        }else{
            r = m
        }
    }
    return 0
}