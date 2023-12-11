class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        c=1
        for i in range(1,n):
            if arr[i-1]==arr[i]:
                c+=1
                if c*4>n:
                    return arr[i]
            else:
                c=1
        return arr[n-1]
        