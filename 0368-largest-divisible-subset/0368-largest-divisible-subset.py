class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1]*n      #length of subset ending cosisting of nums[i]
        prev = [-1]*n   #previous divisble index of nums[i]
        maxlen = 1      #maximum possible length of subset
        maxindex = 0    #index of maxmimum number of subset w
        for i in range(n):
            for j in range(i):
                #if true, nums[i] will be added with subset ended with nums[j]
                if nums[i] % nums[j] == 0:
                    #loop iterate multiple times, so avoid unnecessary increment
                    if dp[i] < dp[j]+1:
                        #subset length increased 1 with nums[i]
                        dp[i] = dp[j]+1
                        #previous divisible nums[j] for iterate subset
                        prev[i] = j
            #new found max len subset 
            if dp[i] > maxlen:
                maxlen = dp[i]
                maxindex = i
        ans=[]
        #print(dp,prev,maxindex)
        #iterate subset from maxmimum to minimum
        while maxindex!=-1:
            ans.append(nums[maxindex])
            maxindex = prev[maxindex]
        return ans