class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0        # count of characters in the subsequence
        value = 0        # current value of the subsequence
        power = 1        # binary place value (2^0, 2^1, 2^2...)

        # process string from right (least significant bit) to left
        for c in reversed(s):
            if c == '0':
                count += 1
            else:
                if value + power <= k:
                    value += power
                    count += 1
            power *= 2

        return count
