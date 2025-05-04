func numEquivDominoPairs(dominoes [][]int) int {
    count := 0
	m := make(map[string]int)

	for _, d := range dominoes {
		a, b := d[0], d[1]
		// create a key where smaller number comes first
		var key string
		if a < b {
			key = strconv.Itoa(a) + "_" + strconv.Itoa(b)
		} else {
			key = strconv.Itoa(b) + "_" + strconv.Itoa(a)
		}

		// if this key already exists, it can pair with each previous one
		count += m[key]
		m[key]++
	}

	return count
}