func zeroFilledSubarray(nums []int) int64 {
    var count int64 = 0
    var consecutive int64 = 0

    for _, num := range nums {
        if num == 0 {
            consecutive++
            count += consecutive // add subarrays ending here
        } else {
            consecutive = 0
        }
    }
    return count
}