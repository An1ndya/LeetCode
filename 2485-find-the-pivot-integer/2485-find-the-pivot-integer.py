class Solution:
    def pivotInteger(self, n: int) -> int:
        prefixsum = [0]*(n+1)
        for i in range(1,n+1):
            #sum from 0 to i numbers 
            prefixsum[i] += i + prefixsum[i-1]
        for i in range(1,n+1):
            #sum from 1 to i numbers
            leftsum = prefixsum[i]
            #sum from i to n numbers
            rightsum = prefixsum[n] - prefixsum[i-1]
            if leftsum == rightsum:
                #pivot
                return i
        #no pivot
        return -1