class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        from bisect import bisect_right

        # Sort events by end time
        events.sort(key=lambda x: x[1])
        n = len(events)

        # Create an array of just end times for binary search
        end_times = [e[1] for e in events]

        # DP table: dp[i][j] = max value using first i events and attending at most j events
        dp = [[0] * (k+1) for _ in range(n+1)]

        for i in range(1, n+1):
            start, end, value = events[i-1]
            # Find last non-overlapping event
            idx = bisect_right(end_times, start-1)

            for j in range(1, k+1):
                # Skip event
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                # Take event
                dp[i][j] = max(dp[i][j], dp[idx][j-1] + value)

        return dp[n][k]
