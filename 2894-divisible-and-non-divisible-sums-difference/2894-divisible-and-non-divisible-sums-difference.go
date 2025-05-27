func differenceOfSums(n int, m int) int {
    // Total sum from 1 to n
	totalSum := n * (n + 1) / 2

	// Count of numbers divisible by m
	k := n / m

	// Sum of numbers divisible by m
	sumDivM := m * (k * (k + 1) / 2)

	// num1 - num2 = totalSum - 2 * sumDivM
	return totalSum - 2*sumDivM
}