// Main function to compute the answer
func maximumLength(nums []int) int {
	isEven := func(x int) bool {
		return x%2 == 0
	}

	// Pattern 1: all even
	evenCount := 0
	for _, num := range nums {
		if isEven(num) {
			evenCount++
		}
	}

	// Pattern 2: all odd
	oddCount := 0
	for _, num := range nums {
		if !isEven(num) {
			oddCount++
		}
	}

	// Pattern 3: even -> odd -> even -> ...
	alt1 := 0
	expectedEven := isEven(nums[0])
	for _, num := range nums {
		if isEven(num) == expectedEven {
			alt1++
			expectedEven = !expectedEven
		}
	}

	// Pattern 4: odd -> even -> odd -> ...
	alt2 := 0
	expectedEven = !isEven(nums[0])
	for _, num := range nums {
		if isEven(num) == expectedEven {
			alt2++
			expectedEven = !expectedEven
		}
	}

	// Return the max of all 4 patterns
	max := evenCount
	if oddCount > max {
		max = oddCount
	}
	if alt1 > max {
		max = alt1
	}
	if alt2 > max {
		max = alt2
	}

	return max
}





