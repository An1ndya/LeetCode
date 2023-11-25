class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        sm=0
        prefixsum = [0]*n
        for i in range(n):
            sm+=nums[i]
            prefixsum[i] =sm
            
        
        result = [0]*n
        result[0]=sm-nums[0]*n
        for i in range(1,n):
            result[i]=nums[i]*i - prefixsum[i-1]
            result[i]+=sm-prefixsum[i]-nums[i]*(n-1-i)
            
        return result
        