func countMaxOrSubsets(nums []int) int {
    maxOr := 0
	for _, num := range nums {
		maxOr |= num
	}

	count := 0
	var dfs func(int, int)
	dfs = func(index int, currentOr int) {
		if index == len(nums) {
			if currentOr == maxOr {
				count++
			}
			return
		}
		// include nums[index]
		dfs(index+1, currentOr|nums[index])
		// exclude nums[index]
		dfs(index+1, currentOr)
	}

	dfs(0, 0)
	return count
}