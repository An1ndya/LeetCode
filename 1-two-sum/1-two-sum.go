func twoSum(nums []int, target int) []int {
    m := make(map[int]int)
    n := len(nums)
    for i:=0;i<n;i++ {

        if value, found := m[target - nums[i]]; found{
            return []int{value,i}
        }    
        m[nums[i]] = i 
    }
    return []int{0,0}
}
        
