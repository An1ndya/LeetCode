class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        n = len(word)

        # Step 1: Compute run-length frequencies
        # Example: 'aaabb' → freq = [3, 2]
        freq = []
        count = 1
        for i in range(1, n):
            if word[i] == word[i - 1]:
                count += 1
            else:
                freq.append(count)
                count = 1
        freq.append(count)  # Append last run's count

        # Step 2: Calculate total possible combinations (without length restriction)
        # For each run of length L, possible choices for original keypresses: 1 to L
        total_combinations = 1
        for run_length in freq:
            total_combinations = total_combinations * run_length % mod

        # Step 3: If number of runs >= k
        # Since each intended character contributes at least 1 to total length,
        # minimum total length is len(freq). If it's already >= k, all combinations are valid.
        if len(freq) >= k:
            return total_combinations

        # Step 4: Use dynamic programming to count the number of ways 
        # where total intended string length is <= k-1 (the "bad" cases)
        #
        # f[s] = number of ways to have total length exactly s
        # g[s] = prefix sum of f[0..s], to enable fast range sum queries
        f = [1] + [0] * (k - 1)  # f[0] = 1, rest zero
        g = [1] * k              # g[0] = 1, prefix sums initialized for 0

        # Process each run
        for run_length in freq:
            f_new = [0] * k  # New DP array for this run
            for total_length in range(1, k):
                # Compute number of ways to get total_length including this run

                # g[total_length-1] is sum of f[0..total_length-1]
                f_new[total_length] = g[total_length - 1]

                # Subtract invalid cases if total_length - run_length - 1 >= 0
                if total_length - run_length - 1 >= 0:
                    f_new[total_length] = (f_new[total_length] - g[total_length - run_length - 1]) % mod

            # Update prefix sums for new DP array
            g_new = [f_new[0]] + [0] * (k - 1)
            for total_length in range(1, k):
                g_new[total_length] = (g_new[total_length - 1] + f_new[total_length]) % mod

            # Move to next state
            f, g = f_new, g_new

        # Step 5: Number of valid combinations = total_combinations - bad_combinations
        bad_combinations = g[k - 1]  # Total number of combinations with length ≤ k-1
        result = (total_combinations - bad_combinations) % mod
        return result
    