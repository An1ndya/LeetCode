func maxFreeTime(eventTime int, startTime []int, endTime []int) int {
	n := len(startTime)

	// canMove[i] indicates whether meeting i can be moved somewhere based on encountered free time
	canMove := make([]bool, n)

	// maxFreeTimeLeft: maximum continuous free time found so far while scanning left-to-right
	// maxFreeTimeRight: same while scanning right-to-left
	maxFreeTimeLeft, maxFreeTimeRight := 0, 0

	// Left-to-right pass
	for i := 0; i < n; i++ {
		// If meeting i's duration can fit into the max free time encountered so far
		if endTime[i]-startTime[i] <= maxFreeTimeLeft {
			canMove[i] = true
		}

		// Update maxFreeTimeLeft:
		if i == 0 {
			// Free time before first meeting
			maxFreeTimeLeft = max(maxFreeTimeLeft, startTime[i])
		} else {
			// Free time between end of previous meeting and start of current
			maxFreeTimeLeft = max(maxFreeTimeLeft, startTime[i]-endTime[i-1])
		}
	}

	// Right-to-left pass
	for i := 0; i < n; i++ {
		meetingIndex := n - i - 1 // Reverse index

		// If meeting's duration can fit into the max free time encountered so far
		if endTime[meetingIndex]-startTime[meetingIndex] <= maxFreeTimeRight {
			canMove[meetingIndex] = true
		}

		// Update maxFreeTimeRight:
		if i == 0 {
			// Free time after last meeting
			maxFreeTimeRight = max(maxFreeTimeRight, eventTime-endTime[n-1])
		} else {
			// Free time between end of next meeting and start of current
			maxFreeTimeRight = max(maxFreeTimeRight, startTime[n-i]-endTime[n-i-1])
		}
	}

	// Now find the maximum continuous free time achievable after rescheduling one meeting
	result := 0
	for i := 0; i < n; i++ {
		// Free time to the left and right of meeting i
		leftBoundary := 0
		if i != 0 {
			leftBoundary = endTime[i-1]
		}

		rightBoundary := eventTime
		if i != n-1 {
			rightBoundary = startTime[i+1]
		}

		// If meeting i is movable, entire interval between neighbors is free
		if canMove[i] {
			result = max(result, rightBoundary-leftBoundary)
		} else {
			// Otherwise — only free time excluding meeting i's duration
			result = max(result, rightBoundary-leftBoundary-(endTime[i]-startTime[i]))
		}
	}

	return result
}

// Helper max function
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
