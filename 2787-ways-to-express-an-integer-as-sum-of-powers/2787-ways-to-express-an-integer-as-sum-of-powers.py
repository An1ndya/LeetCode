class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7  # change if a different modulus intended

        # Build list of x-th powers <= n
        powers = []
        i = 1
        while True:
            p = i ** x
            if p > n:
                break
            powers.append(p)
            i += 1

        # dp[s] = number of ways to make sum s using some subset of powers
        dp = [0] * (n + 1)
        dp[0] = 1

        for p in powers:
            # iterate downwards to preserve uniqueness (each power used at most once)
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]