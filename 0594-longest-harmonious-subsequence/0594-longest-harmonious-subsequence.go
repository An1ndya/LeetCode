func findLHS(nums []int) int {
    count := make(map[int]int)
	maxLength := 0

	// Count frequency of each number
	for _, num := range nums {
		count[num]++
	}

	// Check for harmonious subsequence
	for num, freq := range count {
		if nextFreq, ok := count[num+1]; ok {
			if freq+nextFreq > maxLength {
				maxLength = freq + nextFreq
			}
		}
	}

	return maxLength
}