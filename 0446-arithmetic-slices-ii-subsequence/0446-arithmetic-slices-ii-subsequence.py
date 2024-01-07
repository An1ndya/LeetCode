class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for i in range(n)]
        totalsubsequence=0
        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]
                #store count of 2 sequencial digit count=1 if 2 digit found 
                #count++ for more sequcial digit
                dp[i][diff]+=1
                if diff in dp[j]:
                    #a previous digit nums[j] have same difference sequence with nums[i] 
                    #so atleast 3 digit sequnce, 3 digit: dp[i]= 2 , 4 digit: d[i] = 3 
                    dp[i][diff] += dp[j][diff]
                    #count of dp[j][diff] is count of new found 3 sequence 
                    totalsubsequence += dp[j][diff]
        return totalsubsequence