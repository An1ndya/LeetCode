func findMin(nums []int) int {
    min:= math.MaxInt64
    n:=len(nums)
    l:=0 
    r:=n-1
    
    for l <= r {
        
        //fmt.Println(l, " ",r)
        
        for  l < r && nums[l] == nums[l+1] {l++}
        for  l < r && nums[r] == nums[r-1]  {r--}
        
        m:= int((l+r)/2)
        
        if nums[m] < min { min =nums[m]}
        
        if nums[l] < nums[m] {
            
            if nums[l] < min { min =nums[l]}
            
 
                l = m + 1
            
        }else{
            if nums[r] < min { min = nums[r]}

            r = m - 1
        }
    }
    return min
}