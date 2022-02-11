class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n=len(nums)
        sumarr =[0]*10001
        i=0
        while i<n:
            sumarr[nums[i]]+=nums[i]
            i+=1
            
        for k in range(2,10001): 
            sumarr[k]= max(sumarr[k]+sumarr[k-2],sumarr[k-1])
            
        return sumarr[10000]