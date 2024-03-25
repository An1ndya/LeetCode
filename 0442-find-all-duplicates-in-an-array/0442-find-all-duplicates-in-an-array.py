class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for num in nums:
            #map number n to position n-1 as 0 indexed
            position = abs(num)-1
            #if our mapped positon have a negative number
            #means previous number already mapped and set this position to negative
            #so it duplicate
            if nums[position] < 0:
                ans.append(abs(num))
            #set that position to negative where keep that position value
            nums[position] = - nums[position]
        return ans