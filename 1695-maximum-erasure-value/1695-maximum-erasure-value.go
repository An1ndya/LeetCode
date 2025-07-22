func maximumUniqueSubarray(nums []int) int {
    seen := make(map[int]bool)
    left, currSum, maxSum := 0, 0, 0

    for right := 0; right < len(nums); right++ {
        // If nums[right] already in set, move left pointer
        for seen[nums[right]] {
            seen[nums[left]] = false
            currSum -= nums[left]
            left++
        }
        // Include nums[right] in window
        seen[nums[right]] = true
        currSum += nums[right]
        if currSum > maxSum {
            maxSum = currSum
        }
    }
    return maxSum
}
