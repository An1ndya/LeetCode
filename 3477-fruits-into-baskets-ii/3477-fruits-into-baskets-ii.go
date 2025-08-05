func numOfUnplacedFruits(fruits []int, baskets []int) int {
    n := len(fruits)
	used := make([]bool, n) // to mark which baskets are used

	unplaced := 0
	for i := 0; i < n; i++ {
		placed := false
		for j := 0; j < n; j++ {
			if !used[j] && baskets[j] >= fruits[i] {
				used[j] = true
				placed = true
				break
			}
		}
		if !placed {
			unplaced++
		}
	}
	return unplaced
}