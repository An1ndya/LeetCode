class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        numIndex = {}
        n = len(nums)
        sumWindow = 0
        maxSum = 0
        l = 0
        r = 0
        windowLen = 0
        while r<n:
            if nums[r] not in numIndex:
                numIndex[nums[r]] = r
                sumWindow += nums[r]
                #windowLen = r-l+1
                if r-l+1 == k: 
                    if sumWindow > maxSum: maxSum = sumWindow
                    
                    sumWindow -= nums[l]
                    del numIndex[nums[l]] 
                    l += 1 
            else:
                #assign new left postion where a duplicate exist
                left = numIndex[nums[r]]
                while l <= left:
                    sumWindow -= nums[l]
                    del numIndex[nums[l]] 
                    l += 1
                #update index of current last number
                numIndex[nums[r]] = r
                sumWindow += nums[r]

            r += 1
            #print(numIndex)
        return maxSum
            