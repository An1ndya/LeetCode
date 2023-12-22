class Solution:
    def maxScore(self, s: str) -> int:
        totalzero=0
        totalone=0
        n=len(s)
        mx=0
        for i in range(n):
            if s[i]=='1' : totalone+=1
            else: totalzero +=1
        leftzero, rightone = 0, totalone
        for i in range(n-1):
            if s[i]=='1':
                rightone-=1
            else:
                leftzero+=1
            if rightone+leftzero>mx: mx = leftzero+ rightone
        return mx