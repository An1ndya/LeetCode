func missingNumber(nums []int) int {
    missingone := 0 
    sum := 0
 
    for i:=0;i<len(nums);i++{

        missingone += i+1
        sum += nums[i]

    }
    return missingone - sum
}