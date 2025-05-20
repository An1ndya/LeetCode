func isZeroArray(nums []int, queries [][]int) bool {
    n := len(nums)
	// Step 1: Create a difference array (size n+1 for safe indexing)
	// diff[i] will eventually tell us how many times nums[i] is covered by queries
	diff := make([]int, n+1)

	// Step 2: Process all queries using the difference array technique
	// For each query [l, r], we increment diff[l] by 1
	// and decrement diff[r+1] by 1 (if it's within bounds)
	for _, query := range queries {
		l, r := query[0], query[1]
		diff[l] += 1
		if r+1 < n {
			diff[r+1] -= 1
		}
	}
	// Step 3: Build coverage array using prefix sum from diff array
	// coverage[i] tells us how many times nums[i] is affected by the queries
	coverage := make([]int, n)
	coverage[0] = diff[0]
	for i := 1; i < n; i++ {
		coverage[i] = coverage[i-1] + diff[i]
	}
	// Step 4: Check if each nums[i] can be decremented to 0
	// i.e., nums[i] should not be greater than coverage[i]
	for i := 0; i < n; i++ {
		if nums[i] > coverage[i] {
			return false
		}
	}

	// If all checks pass, return true
	return true
}