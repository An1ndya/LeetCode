func divideString(s string, k int, fill byte) []string {
    var result []string
	n := len(s)

	for i := 0; i < n; i += k {
		end := i + k
		if end > n {
			end = n
		}
		group := s[i:end]

		// if last group is shorter than k, fill with 'fill' character
		if len(group) < k {
			group += strings.Repeat(string(fill), k-len(group))
		}

		result = append(result, group)
	}

	return result
}