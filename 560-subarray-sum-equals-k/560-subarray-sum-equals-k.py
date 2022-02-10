class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0
        d={0:1} #sum 0, occurance 1
        sm=0
        for num in nums:
            sm += num
            if sm-k in d:
                ans+=d[sm-k] 
            if sm in d:
                d[sm]+=1
            else:
                d[sm]=1
        return ans