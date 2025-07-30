func longestSubarray(nums []int) int {
    maxVal := nums[0]
    
    // Step 1: Find the maximum value in the array
    for _, num := range nums {
        if num > maxVal {
            maxVal = num
        }
    }

    maxLen := 0
    currLen := 0

    // Step 2: Find the longest contiguous subarray with value == maxVal
    for _, num := range nums {
        if num == maxVal {
            currLen++
            if currLen > maxLen {
                maxLen = currLen
            }
        } else {
            currLen = 0
        }
    }

    return maxLen
}
