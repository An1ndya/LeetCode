class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n=len(nums)
        d={}
        ans=0
        for i in nums:
            if k==0:
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
                if d[i]==2: ans+=1
            else:    
                if i not in d:
                    a=i+k
                    b=i-k

                    if a in d: ans+=1
                    if b in d: ans+=1

                d[i]=True

        return ans