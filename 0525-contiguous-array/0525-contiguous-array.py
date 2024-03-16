class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
       
        mx=0
        count=0  # count of 1 minus counnt of zero
        countToIndex = {0:-1} #index set to -1 before start to length calculation correctly
        for i in range(len(nums)):
            if nums[i] == 1 : 
                count +=1
            else: 
                count -=1
            # for equal zero and one, count = 0
            #previously occured mean we found a subsequence 
            #length = current - old index 
            #between same count There is definitely a subsequence with equal count of 0,1 
            if count in countToIndex:
                mx=max(mx, i-countToIndex[count])
                #wont update as oldest index have maximum subsequence
            else:
                #as not present we need to update this first occurance 
                countToIndex[count] = i
                
        return mx        