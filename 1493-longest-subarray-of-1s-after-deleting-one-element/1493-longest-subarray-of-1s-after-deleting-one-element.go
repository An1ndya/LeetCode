func longestSubarray(nums []int) int {
    left, zeros, maxLen := 0, 0, 0

    for right := 0; right < len(nums); right++ {
        if nums[right] == 0 {
            zeros++
        }

        // If more than one zero in window, shrink from left
        for zeros > 1 {
            if nums[left] == 0 {
                zeros--
            }
            left++
        }

        // Track window length
        maxLen = max(maxLen, right-left+1)
    }

    return maxLen - 1  // must delete one element
}
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}