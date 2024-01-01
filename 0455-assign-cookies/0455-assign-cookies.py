class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        #print(g,s)
        gi,si,ans=0,0,0
        while gi< len(g) and si<len(s):
            if g[gi]<=s[si]:
                gi+=1
                si+=1
                ans+=1
            else:
                si+=1
        return ans
                