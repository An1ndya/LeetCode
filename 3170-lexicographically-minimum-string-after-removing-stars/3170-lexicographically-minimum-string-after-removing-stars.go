func clearStars(s string) string {
    // Convert string to []byte for mutability
	sb := []byte(s)

	// 26 stacks for 'a' to 'z' → each a slice of int (indices)
	stacks := make([][]int, 26)

	for i := 0; i < len(sb); i++ {
		ch := sb[i]
		if ch != '*' {
			// Push index to corresponding character's stack
			idx := ch - 'a'
			stacks[idx] = append(stacks[idx], i)
		} else {
			// Remove smallest available character (check stacks from 'a' to 'z')
			for j := 0; j < 26; j++ {
				if len(stacks[j]) > 0 {
					// Pop the last index from this stack
					lastIdx := stacks[j][len(stacks[j])-1]
					stacks[j] = stacks[j][:len(stacks[j])-1]
					// Mark removed character in sb
					sb[lastIdx] = '#'
					break
				}
			}
		}
	}

	// Build result string (skip '*' and '#')
	result := make([]byte, 0, len(sb))
	for _, ch := range sb {
		if ch != '*' && ch != '#' {
			result = append(result, ch)
		}
	}

	return string(result)
}