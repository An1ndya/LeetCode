func reorderedPowerOf2(n int) bool {
    sigN := signature(n)
    for i := 0; i < 31; i++ { // 2^30 < 1e9
        if sigN == signature(1<<i) {
            return true
        }
    }
    return false
}

func signature(x int) string {
    digits := []byte(strconv.Itoa(x))
    sort.Slice(digits, func(i, j int) bool {
        return digits[i] < digits[j]
    })
    return string(digits)
}
