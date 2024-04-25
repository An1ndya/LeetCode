class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp =[0]*26 # length of ideal string ending with i. ex i=2->'c'
        maxcount = 0 
        for char in s:
            pos = ord(char) - ord('a')
            sequencecount = 0
            for i in range(26):
                #char can be included to sequence
                if abs(i-pos) <= k:
                    sequencecount = max(sequencecount, dp[i])
            #char can be added to ideal, sequencecount+1 can might answer
            dp[pos] = max(dp[pos], sequencecount+1)
            maxcount = max(dp[pos], maxcount)
        return maxcount