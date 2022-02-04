class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
       
        mx=0
        c=0
        hashtable = {0:-1} #index set to -1 befor start
        for i in range(len(nums)):
            if nums[i] == 1 : 
                c +=1
            else: 
                c -=1
            if c in hashtable:
                mx=max(mx, i-hashtable[c])
            else:
                hashtable[c] = i
                
        return mx        