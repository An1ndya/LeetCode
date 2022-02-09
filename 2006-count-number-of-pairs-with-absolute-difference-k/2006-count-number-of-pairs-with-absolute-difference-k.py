class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        d={}
        ans=0
        for i in nums:
            if i not in d: d[i]=1
            else: d[i]+=1
                
            a=i+k
            b=i-k

            if a in d: ans+=d[a]
            if b in d: ans+=d[b]
                
        return ans      