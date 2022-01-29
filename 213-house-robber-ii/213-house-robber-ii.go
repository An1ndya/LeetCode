func rob(nums []int) int {
    
    n := len(nums)
    
    if n==1{return nums[0]}
    
    ara:= make([]int, n+2)
    
    ara[0] = nums[0]

    ara[1] = max(nums[0],nums[1])
    
    if n==2 {return ara[1]}
    
    for i:=2;i<n-1;i++{
        ara[i] = max(ara[i-1], ara[i-2]+nums[i])
       
    }
    mx:=ara[n-2]
    
    ara[1] = nums[1]

    ara[2] = max(nums[2],nums[1])
    
    for i:=3;i<n;i++{
        ara[i] = max(ara[i-1], ara[i-2]+nums[i])
       
    }
    return max(mx,ara[n-1])
}
func max(a int, b int ) int{
    if a > b{
        return a
    }else{
        return b
    }
}