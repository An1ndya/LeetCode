class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        n=len(nums)
        for i in nums:
            if i in d: return True
            d[i]=True
        return False