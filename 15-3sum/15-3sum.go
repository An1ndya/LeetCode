func threeSum(nums []int) [][]int {
    
    triplets := [][]int{}
    sort.Ints(nums)
    n:= len(nums)
    
    for i:=0;i<n;i++{
        
        if nums[i] > 0 {continue}
        if i > 0 && nums[i] == nums[i-1] {continue}
        
        left, right := i+1, n-1
        
        for left < right{
    
            sum := nums[i] + nums[left] + nums[right]
            
            if sum == 0 {
                
                triplets = append(triplets,[]int{nums[i],nums[left],nums[right]}) 
                
                for left < right && nums[left]==nums[left+1] {left++}
                for left < right && nums[right]==nums[right-1] {right--}
                
                //need point to next no equal value
                left++
                right--
                  
            }else if sum > 0 {
                right--   
            }else {     //sum < 0
                left++
            }
        }   
    }

    return triplets
}