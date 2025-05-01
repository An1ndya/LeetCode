func maxTaskAssign(tasks []int, workers []int, pills int, strength int) int {
	// sort both lists so we can do two‐pointer / binary‐search assignments
	sort.Ints(tasks)
	sort.Ints(workers)

	// canAssign(k) checks if we can complete the k hardest tasks
	canAssign := func(k int) bool {
		// take the k strongest workers
		avail := make([]int, k)
		copy(avail, workers[len(workers)-k:])
		remainingPills := pills

		// iterate tasks from hardest → easiest (end of sorted tasks slice)
		for i := k - 1; i >= 0; i-- {
			req := tasks[i]
			// 1) try to use the strongest available worker without a pill
			if avail[len(avail)-1] >= req {
				avail = avail[:len(avail)-1] // pop strongest
				continue
			}
			// 2) else, see if we can use a pill
			if remainingPills == 0 {
				return false
			}
			// find the *smallest* w in avail such that w + strength >= req
			need := req - strength
			// binary search for lower_bound(avail, need)
			l, r := 0, len(avail)
			for l < r {
				m := (l + r) / 2
				if avail[m] < need {
					l = m + 1
				} else {
					r = m
				}
			}
			if l == len(avail) {
				// no worker that can reach req even with a pill
				return false
			}
			// use that worker with a pill
			avail = append(avail[:l], avail[l+1:]...)
			remainingPills--
		}
		return true
	}

	// binary search on the answer ∈ [0, min(len(tasks), len(workers))]
	lo, hi := 0, min(len(tasks), len(workers))
	ans := 0
	for lo <= hi {
		mid := (lo + hi) / 2
		if canAssign(mid) {
			ans = mid   // feasible → try for more
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return ans
}

// min helper function
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

