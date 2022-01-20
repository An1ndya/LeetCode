func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    n := len(nums)
    for i:=0;i<n;i++ {
        
        if value, found := m[nums[i]]; found {
            //same element found 
            //check if match target
            if 2*nums[i] == target {
                return []int{value,i}
            }
        }else{
            complement := target - nums[i]
            
            if value, found := m[complement]; found{
                return []int{value,i}
            }    
            
            m[nums[i]] = i
        }
    }
    return []int{0,0}
}
        
