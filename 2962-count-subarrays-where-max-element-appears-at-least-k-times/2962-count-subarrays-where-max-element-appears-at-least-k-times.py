class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
             
        n = len(nums)
        mx = max(nums)
        maxcount = 0
        ans = 0
        
        start = 0 #subarray start index
        end = 0   #subarray end index
        #between start and end window there should be exact k elements 
        
        while end < n:
            if nums[end] == mx:
                #if max element found increase count in window
                maxcount += 1
            end += 1
            while maxcount == k:
                #when exact maxcount found, 
                #identify start position of window with last k max elements 
                if nums[start] == mx:
                    maxcount -= 1
                start += 1
            #there can be 0,1..,start-1 starting position of subaarays with k max elemets 
            #when k window not found start set as 0, so adding them cause no change
            #if start unchanged, then last added element in window 
            #will create previous count(start) subarrays with same logic
            ans += start    
        return ans