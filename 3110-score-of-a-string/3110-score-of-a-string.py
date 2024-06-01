class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        score = 0
        prev = ord(s[0])
        for i in range(1,n):
            cur = ord(s[i])
            score += abs(prev- cur)
            prev = cur
        return score