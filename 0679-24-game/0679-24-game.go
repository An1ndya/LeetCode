func judgePoint24(cards []int) bool {
    	const EPS = 1e-6

	// recursive DFS
	var dfs func([]float64) bool
	dfs = func(nums []float64) bool {
		if len(nums) == 1 {
			return math.Abs(nums[0]-24) < EPS
		}

		n := len(nums)
		for i := 0; i < n; i++ {
			for j := i + 1; j < n; j++ {
				a, b := nums[i], nums[j]
				next := make([]float64, 0, n-1)
				for k := 0; k < n; k++ {
					if k != i && k != j {
						next = append(next, nums[k])
					}
				}

				results := []float64{a + b, a - b, b - a, a * b}
				if math.Abs(b) > EPS {
					results = append(results, a/b)
				}
				if math.Abs(a) > EPS {
					results = append(results, b/a)
				}

				for _, res := range results {
					if dfs(append(next, res)) {
						return true
					}
				}
			}
		}
		return false
	}

	nums := make([]float64, 4)
	for i := range cards {
		nums[i] = float64(cards[i])
	}
	return dfs(nums)
}