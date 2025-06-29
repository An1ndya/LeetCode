func numSubseq(nums []int, target int) int {
    const MOD = 1e9 + 7
    n := len(nums)
    sort.Ints(nums)

    // Precompute powers of 2 up to n
    pow2 := make([]int, n+1)
    pow2[0] = 1
    for i := 1; i <= n; i++ {
        pow2[i] = (pow2[i-1] * 2) % MOD
    }

    ans := 0
    l, r := 0, n-1
    for l <= r {
        if nums[l]+nums[r] <= target {
            // All subsequences where nums[l] is min, and any subset of
            // nums[l+1..r] chosen freely, will have max ≤ nums[r].
            ans = (ans + pow2[r-l]) % MOD
            l++
        } else {
            // Too large sum, decrease the max end
            r--
        }
    }

    return ans
}