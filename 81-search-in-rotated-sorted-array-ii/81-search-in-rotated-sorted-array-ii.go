func search(nums []int, target int) bool {
        
    n:=len(nums)
    l:=0 
    r:=n-1
    

    return binarysearch(nums, l, r, target)
}
func binarysearch(nums []int, l int, r int, t int) bool{
    
    if l > r {return false}
    //fmt.Println(l," ",r)
    
    m:= int((l+r)/2)

    if nums[m] == t{ return true }

    if nums[r] == t  { return true}
    
    if nums[l]==nums[m] && nums[r]==nums[m]  {
        return binarysearch(nums, l, m-1, t) || binarysearch(nums, m+1, r, t)
    }else if nums[l] == nums[m] {
        return binarysearch(nums, m+1, r, t)
    }else if  nums[r] == nums[m] {
        return binarysearch(nums, l, m-1, t)
    }else if nums[l] < nums[m] {
        if t < nums[m] && t >= nums[l]{
            r = m - 1 
        }else{
            l = m + 1
        }
        return binarysearch(nums, l, r, t)
    }else{
        if t > nums[m] && t <= nums[r]{
            l = m + 1 
        }else{
            r = m - 1        
        }
        return binarysearch(nums, l, r, t)
    }
    
}