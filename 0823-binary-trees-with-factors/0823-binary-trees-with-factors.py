class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        n=len(arr)
        dp={}
        sum=0
        for i in arr:
            dp[i]=1
        #if dividend is different the same value updated two time
        #so left , right child combination counted
        #if dividend and divisor same it will sum up once
        for i in range(n):
            for j in range(n-1):
                if arr[i]%arr[j]==0:
                    dividend = int(arr[i]/arr[j])
                    if dividend in dp:
                        dp[arr[i]]+=dp[arr[j]]*dp[dividend]
            sum= (sum+dp[arr[i]])%1000000007
        return sum