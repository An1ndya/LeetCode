from collections import defaultdict 
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums: 
            count[num]+=1
        ans=0
        for num in count.keys():
            if count[num] == 1:
                return -1
            elif count[num]%3 == 0:
                ans+= count[num]//3
            else:
                ans+=count[num]//3+1
        return ans