class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        minIndex, maxIndex, OutsideRangeIndex = -1,-1,-1
        count = 0
        #iteration of suarray including every nums[i]
        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                OutsideRangeIndex = i
            if nums[i] == minK:
                minIndex =  i
            if nums[i] == maxK:
                maxIndex =  i
            #if both min and max exist
            if minIndex != -1 and maxIndex != -1:
                #to include both we need to take initial position of minimum index
                foremostofBoth = min(minIndex, maxIndex)
                if OutsideRangeIndex < foremostofBoth:
                    #smaller outside element means 
                    #between foremostofBoth and i there is subarray with mink and maxk
                    #now including i last, 
                    #subarray can start from OutsideRangeIndex+1,...,foremostofBoth postion
                    #including i following number of fixed-bound subarry can be found
                    count += foremostofBoth - OutsideRangeIndex
        return count