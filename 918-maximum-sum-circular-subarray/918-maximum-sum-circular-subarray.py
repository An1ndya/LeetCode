class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        smx=0
        smn=0
        t=0
        mx=-100000
        mn= 100000
        n=len(nums)
        for i in nums:
            t+=i
            smx+=i
            smn+=i
            if smx>mx: mx=smx
            if smx<0: smx=0  
                
            if smn<mn : mn=smn
            if smn>0: smn=0 
       
        return max(mx,t-mn) if t!=mn else mx