class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 : return 0
        step=0
        curstepend=0
        mx=0
        for i in range(0,n,1):
            
            mx=max(mx,i+nums[i])
            
            if curstepend==i: 
                step+=1
                curstepend=mx
                if curstepend>=n-1:
                    break
        return step     