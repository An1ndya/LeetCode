func maximum69Number (num int) int {
    // Convert to string
	s := strconv.Itoa(num)
	// Replace only the first "6" with "9"
	s = strings.Replace(s, "6", "9", 1)
	// Convert back to int
	result, _ := strconv.Atoi(s)
	return result
}