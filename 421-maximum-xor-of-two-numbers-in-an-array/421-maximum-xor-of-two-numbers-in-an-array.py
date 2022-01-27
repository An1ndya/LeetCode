class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        mx = 0
        mask =0
        for i in range(31,-1,-1):
            mask |= 1 <<i 
            Dict = {}
            c = mx | 1<<i
            for j in range(n):
                bitnum = mask & nums[j]
                if bitnum^c in Dict:
                    mx = c
                    break
                else:
                    Dict[bitnum] = True
        return mx