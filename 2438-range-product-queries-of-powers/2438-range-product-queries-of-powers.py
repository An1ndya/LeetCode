class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
       # collect bit positions (exponents) in ascending order
        exps = []
        k = 0
        x = n
        while x:
            if x & 1:
                exps.append(k)
            x >>= 1
            k += 1

        # prefix sums of exponents
        pref = [0] * len(exps)
        for i, e in enumerate(exps):
            pref[i] = e + (pref[i-1] if i else 0)

        res = []
        for l, r in queries:
            exp_sum = pref[r] - (pref[l-1] if l else 0)
            res.append(pow(2, exp_sum, MOD))
        return res
