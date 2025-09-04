func findClosest(x int, y int, z int) int {
    d1 := int(math.Abs(float64(x - z)))
	d2 := int(math.Abs(float64(y - z)))

	if d1 < d2 {
		return 1
	} else if d2 < d1 {
		return 2
	} else {
		return 0
	}
}