class Solution:
    def trailingZeroes(self, n: int) -> int:
        powerof5=5
        trailingzeros = 0
        while(powerof5<=n):
            trailingzeros += n//powerof5
            powerof5 *= 5
        return trailingzeros
            