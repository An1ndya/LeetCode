class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        n = len(s)
        sum = hash[s[n-1]]
        for i in range(n-2,-1,-1):
            if hash[s[i]]>=hash[s[i+1]]:
                sum+=hash[s[i]]
            else:
                sum-=hash[s[i]]
        return sum
        