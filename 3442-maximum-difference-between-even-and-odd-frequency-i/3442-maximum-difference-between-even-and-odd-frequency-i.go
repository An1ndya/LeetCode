func maxDifference(s string) int {
    freq := make(map[rune]int)

	// Count character frequencies
	for _, ch := range s {
		freq[ch]++
	}

	maxOdd := math.MinInt32
	minEven := math.MaxInt32

	for _, count := range freq {
		if count%2 == 1 { // odd frequency
			if count > maxOdd {
				maxOdd = count
			}
		} else { // even frequency
			if count < minEven {
				minEven = count
			}
		}
	}

	// If no odd or no even frequency exists, we can't calculate diff
	if maxOdd == math.MinInt32 || minEven == math.MaxInt32 {
		return 0
	}

	return maxOdd - minEven
}