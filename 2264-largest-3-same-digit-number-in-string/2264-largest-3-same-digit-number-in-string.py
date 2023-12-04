class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        count=1
        mx=-1
        for i in range(1,n):
            if num[i]==num[i-1]:
                count+=1
                if count>=3:
                    mx=max(mx,int(num[i-1]))
            else:
                count=1
        if mx>-1:   return 3*str(mx)
        return ""