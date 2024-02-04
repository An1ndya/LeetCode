class Solution:
    def minWindow(self, s: str, t: str) -> str:
        notcovered = len(t)
        charcount = {}
        for c in t:
            if c in charcount:
                charcount[c] += 1
            else:
                charcount[c] = 1
        l=0
        r=0
        minlen = 1000000
        ans = ""
        while r < len(s):
            if s[r] in charcount:
                charcount[s[r]]-=1
                if charcount[s[r]] >=0:
                    notcovered -= 1
                
            r+=1
            while notcovered <= 0:
            
                length = r-l;
                if (length < minlen ):
                    minlen = length
                    ans= s[l:r]
                if s[l] in charcount:
                    charcount[s[l]] +=1
                    if charcount[s[l]] > 0:
                        notcovered += 1
                l+=1 
            
        return ans