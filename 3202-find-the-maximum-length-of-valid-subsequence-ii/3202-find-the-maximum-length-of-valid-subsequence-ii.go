func maximumLength(nums []int, k int) int {
	n := len(nums)
	maxLen := 0

	// Try all possible (a + b) % k values
	for modVal := 0; modVal < k; modVal++ {
		length := 1
		prev := nums[0]

		for i := 1; i < n; i++ {
			sum := prev + nums[i]
			if sum%k == modVal {
				length++
				prev = nums[i]
			}
		}

		if length > maxLen {
			maxLen = length
		}
	}

	return maxLen
}

