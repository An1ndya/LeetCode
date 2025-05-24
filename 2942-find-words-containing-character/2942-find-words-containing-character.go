func findWordsContaining(words []string, x byte) []int {
	var result []int
	for i, word := range words {
		for _, ch := range word {
			if byte(ch) == x {
				result = append(result, i)
				break // no need to check rest of the word
			}
		}
	}
	return result
}