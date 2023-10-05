class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hash ={}
        n=len(nums)
        for i in nums:
            if i in hash: hash[i]+=1
            else: hash[i]=1
        ans =[]
        for i in hash:
            if 3*hash[i]>n:
                ans.append(i)
        return ans