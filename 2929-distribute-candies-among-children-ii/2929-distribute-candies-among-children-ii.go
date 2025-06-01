func distributeCandies(n, limit int) int64 {
	total := int64(0)

	for i := 0; i <= min(limit, n); i++ {
		minJ := max(0, n-i-limit)
		maxJ := min(limit, n-i)
		if minJ <= maxJ {
			total += int64(maxJ - minJ + 1)
		}
	}

	return total
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}