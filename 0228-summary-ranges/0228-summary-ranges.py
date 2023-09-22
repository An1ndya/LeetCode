class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n= len(nums)
        ans=[]
        i=0
        while i<n:
            l=i
            while i< n-1 and nums[i]+1==nums[i+1] :
                i+=1
                       
            if l==i :  ans.append(str(nums[i]))
            else   :  ans.append(str(nums[l]) +"->" +str(nums[i]))
                
            i+=1
        return ans