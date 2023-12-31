
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        firstpos = {}
        mx=-1
        for i in range(len(s)):
            if s[i] not in firstpos:
                firstpos[s[i]] = i
            
            mx = max(mx,i-firstpos[s[i]]-1)
          
        return mx
            
        
        