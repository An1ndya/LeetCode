class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        subarrayfrequency = defaultdict(int) # frequency in subarray
        n = len(nums)
        start = 0 #subarray start index
        end = 0   #subarray end index
        maxlength = 0
        while end < n:
            subarrayfrequency[nums[end]] += 1
            if subarrayfrequency[nums[end]] <= k:
                #last element count is less than equal to k, so we will check next element 
                end += 1
            else:
                #print(start, end)
                #Last element at end postion count > k
                #so we will come from start until we find same number at end postion
                while nums[start] != nums[end]:
                    subarrayfrequency[nums[start]] -= 1
                    start += 1
                #we found first occurance of start in subarray which is equal to nums[end]
                #we have to discount this element so nums[end] count become = k
                subarrayfrequency[nums[start]] -= 1
                start += 1
                #end postion's count have already considered 
                #so set end to next postion
                end += 1
                
            length = end - start 
            if length > maxlength: maxlength = length
        return maxlength