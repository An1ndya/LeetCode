class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        #place 1 at 0 , 2 at 1 and 3 at 2 etc postion
        #0 or greater than n values postion 
        i = 0
        while i < n:
            position = nums[i]-1
            if 1 <= nums[i] <= n and nums[position] != nums[i]:
                #swap to position the number at mapped position 
                nums[i], nums[position] = nums[position], nums[i]
                #we need to do same position check new element in i psotion 
                #so keep i same
            else:
                i += 1
    
        for i in range(n):
            # i+1 is least number not in postioned place, so it least number
            if nums[i] != i+1:
                return i+1
        return n+1

