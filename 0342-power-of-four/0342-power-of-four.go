func isPowerOfFour(n int) bool {
    // condition 1: positive number
    if n <= 0 {
        return false
    }
    // condition 2: power of two (only one bit set)
    if n&(n-1) != 0 {
        return false
    }
    // condition 3: bit in even position (0x55555555 is binary mask 010101...)
    return (n & 0x55555555) != 0
}