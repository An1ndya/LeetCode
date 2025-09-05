class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):  # Up to 60 operations
            S = num1 - k * num2
            if S < 0:
                continue
            # Check binary constraints
            if S >= k and bin(S).count('1') <= k:
                return k
        return -1 