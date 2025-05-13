func lengthAfterTransformations(s string, t int) int {
    const MOD = 1e9 + 7
    // count of each character 'a' to 'z'
	count := make([]int, 26)
	for _, ch := range s {
		count[ch-'a']++
	}

	for i := 0; i < t; i++ {
		newCount := make([]int, 26)
		for j := 0; j < 26; j++ {
			if j == 25 { // 'z'
				newCount[0] = (newCount[0] + count[25]) % int(MOD) // 'a'
				newCount[1] = (newCount[1] + count[25]) % int(MOD) // 'b'
			} else {
				newCount[j+1] = (newCount[j+1] + count[j]) % int(MOD)
			}
		}
		count = newCount
	}

	// sum up the final counts
	result := 0
	for _, c := range count {
		result = (result + c) % int(MOD)
	}

	return result
}