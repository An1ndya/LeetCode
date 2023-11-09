class Solution:
    def countHomogenous(self, s: str) -> int:
        mod=1000000007
        n =len(s)
        ans=1
        c=1
        for i in range(1,n):
            if s[i-1]==s[i]:
                c+=1
            else:
                c=1
            ans+=c
            ans=ans % mod
            
        return ans