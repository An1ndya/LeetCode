func maximumDifference(nums []int) int {
    minVal := nums[0]
    maxDiff := -1

    for i := 1; i < len(nums); i++ {
        if nums[i] > minVal {
            diff := nums[i] - minVal
            if diff > maxDiff {
                maxDiff = diff
            }
        } else {
            minVal = nums[i]
        }
    }
    return maxDiff
}