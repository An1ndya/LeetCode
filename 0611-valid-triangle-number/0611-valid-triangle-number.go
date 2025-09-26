func triangleNumber(nums []int) int {
    sort.Ints(nums)
    n := len(nums)
    count := 0

    for k := n - 1; k >= 2; k-- {
        i, j := 0, k-1
        for i < j {
            if nums[i] + nums[j] > nums[k] {
                count += (j - i)
                j--
            } else {
                i++
            }
        }
    }
    return count
}
