func possibleStringCount(word string) int {
    	n := len(word)
	if n == 0 {
		return 1 // only the empty string itself
	}

	total := 1 // start with 1 for the “no mistake” scenario
	i := 0

	for i < n {
		j := i
		for j < n && word[j] == word[i] {
			j++
		}
		groupLen := j - i
		if groupLen > 1 {
			// if this group was the mistake, you could have intended any length from 1 to groupLen-1
			total += groupLen - 1
		}
		i = j
	}

	return total
}