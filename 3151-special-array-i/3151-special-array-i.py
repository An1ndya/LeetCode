class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        parity = bool(nums[0]%2)  #parity of last number
        for i in range(1,n):

            if parity == bool(nums[i]%2):
                # same parity with last one
                return False
            # revert to check with next number
            parity = not parity 
        return True
