func maxDiff(num int) int {
    strNum := strconv.Itoa(num)

	// Create maxA by replacing first non-9 digit with 9
	var maxA string
	for i := 0; i < len(strNum); i++ {
		if strNum[i] != '9' {
			maxA = strings.ReplaceAll(strNum, string(strNum[i]), "9")
			break
		}
	}
	if maxA == "" {
		maxA = strNum // already all 9's
	}

	// Create minB
	var minB string
	// If first digit isn't 1, replace it with 1
	if strNum[0] != '1' {
		minB = strings.ReplaceAll(strNum, string(strNum[0]), "1")
	} else {
		// Else, replace first digit not 0 or 1 with 0
		for i := 1; i < len(strNum); i++ {
			if strNum[i] != '0' && strNum[i] != '1' {
				minB = strings.ReplaceAll(strNum, string(strNum[i]), "0")
				break
			}
		}
	}
	if minB == "" {
		minB = strNum
	}

	// Convert to integers and calculate difference
	a, _ := strconv.Atoi(maxA)
	b, _ := strconv.Atoi(minB)

	return a - b
}