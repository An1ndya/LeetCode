func kthCharacter(k int) byte {
    // Recursive helper function
	var helper func(k int, currentChar byte) byte
	helper = func(k int, currentChar byte) byte {
		if k == 1 {
			return currentChar
		}
		// Find the length of word before it crosses k
		length := 1
		for length*2 < k {
			length *= 2
		}
		if k <= length {
			// If k is in the first half
			return helper(k, currentChar)
		} else {
			// If k is in the second half
			ch := helper(k-length, currentChar)
			// Get next character
			return (ch-'a'+1)%26 + 'a'
		}
	}

	return helper(k, 'a')
}