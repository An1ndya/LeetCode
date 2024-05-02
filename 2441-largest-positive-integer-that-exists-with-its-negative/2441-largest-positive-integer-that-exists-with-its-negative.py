class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        negative = {}
        mx = -1
        #first pass to save negative value
        for num in nums:
            if num < 0:
                negative[num] = True
        #2nd pass to find max
        for num in nums:
            if num > mx:
                if -num in negative:
                    mx = num           
        return mx