class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarraysWithAtMostKDistinct(nums, k) -> int:
            n = len(nums)
            numberCount = defaultdict(int)
            distinctIntegerCount = 0 #count of distint integer
            start = 0 #subarray start index
            end = 0   #subarray end index
            subarrayCount = 0 # count of total subarray
            while end < n:
                #increase last element frequency / count in window
                numberCount[nums[end]] += 1
                #if it is a new element increase distinct integer count
                if numberCount[nums[end]] == 1: distinctIntegerCount += 1
                #if last element is new, and increase count of distinct integer
                #need to reduce window size(until k distinct) by increasing start 
                while distinctIntegerCount > k:
                    numberCount[nums[start]] -= 1
                    if numberCount[nums[start]] == 0: distinctIntegerCount -= 1
                    start += 1
                #between start and end window, there is exactly end - start + 1 subarray
                #that have distinct integer less than or equal to k 
                #where end is always included and start position from start,....,to end 
                subarrayCount += end - start + 1
                end += 1
            return subarrayCount
        #exact k can be found by using subarray count of at most k disntinct 
        return subarraysWithAtMostKDistinct(nums,k) - subarraysWithAtMostKDistinct(nums,k-1)