func new21Game(n int, k int, maxPts int) float64 {
        if k == 0 || n >= k-1+maxPts {
        return 1.0
    }
    dp := make([]float64, n+1)
    dp[0] = 1.0
    window := 1.0
    ans := 0.0

    for i := 1; i <= n; i++ {
        dp[i] = window / float64(maxPts)
        if i < k {
            window += dp[i]
        } else {
            ans += dp[i]
        }
        j := i - maxPts
        if j >= 0 && j < k {
            window -= dp[j]
        }
    }
    return ans
}