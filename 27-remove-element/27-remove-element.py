class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=0
        p=0
        while i<len(nums):
            if nums[i]==val:
                p+=1
            else:
                if p>0 : nums[i-p]=nums[i]   
            i+=1
            
        return n-p