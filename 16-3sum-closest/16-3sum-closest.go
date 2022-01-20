func threeSumClosest(nums []int, target int) int {
    
    minsum := 0
    mindiff := math.MaxInt64
    sort.Ints(nums)
    n:= len(nums)
    
    for i:=0;i<n;i++{
              
        if i > 0 && nums[i] == nums[i-1] {continue}
        
        left, right := i+1, n-1
        
        for left < right{
            
            sum := nums[i] + nums[left] + nums[right]
            //fmt.Println(i," ", left," ",right, " ",sum)
            if sum == target {        
                return sum   
            }else if sum > target {
                right--   
            }else {                 //sum < target
                left++
            }
            diff := Abs(target - sum)
            
            if diff < mindiff {
                mindiff = diff
                minsum =sum
            } 
        }   
    }
    return minsum
}

func Abs(x int) int {
	if x < 0 { return -x}
	return x
}