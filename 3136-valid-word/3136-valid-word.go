func isValid(word string) bool {
	if len(word) < 3 {
		return false
	}

	hasVowel := false
	hasConsonant := false

	for _, ch := range word {
		if !unicode.IsLetter(ch) && !unicode.IsDigit(ch) {
			return false
		}
		if unicode.IsLetter(ch) {
			if isVowel(ch) {
				hasVowel = true
			} else {
				hasConsonant = true
			}
		}
	}

	return hasVowel && hasConsonant
}

func isVowel(ch rune) bool {
	switch unicode.ToLower(ch) {
	case 'a', 'e', 'i', 'o', 'u':
		return true
	default:
		return false
	}
}

