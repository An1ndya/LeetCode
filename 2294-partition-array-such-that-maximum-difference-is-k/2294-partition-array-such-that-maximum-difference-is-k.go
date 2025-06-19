func partitionArray(nums []int, k int) int {
    sort.Ints(nums)
	count := 1
	start := nums[0]

	for _, num := range nums {
		if num-start > k {
			count++
			start = num
		}
	}

	return count
}