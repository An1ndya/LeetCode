func candy(ratings []int) int {
    n := len(ratings)
	candies := make([]int, n)

	// Each child gets at least one candy
	for i := range candies {
		candies[i] = 1
	}

	// Left to Right
	for i := 1; i < n; i++ {
		if ratings[i] > ratings[i-1] {
			candies[i] = candies[i-1] + 1
		}
	}

	// Right to Left
	for i := n - 2; i >= 0; i-- {
		if ratings[i] > ratings[i+1] && candies[i] <= candies[i+1] {
			candies[i] = candies[i+1] + 1
		}
	}

	// Sum total candies
	total := 0
	for _, c := range candies {
		total += c
	}

	return total
}