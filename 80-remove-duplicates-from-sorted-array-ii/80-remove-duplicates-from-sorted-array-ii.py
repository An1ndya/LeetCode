class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=1
        c=0
        d=0
        p=0
        while i<len(nums):
            if nums[i]==nums[i-1]:
                c+=1
            else:
                c=0
            if c<2: p+=1
            if p<i : nums[p]=nums[i]       
            i+=1
            
        return p+1