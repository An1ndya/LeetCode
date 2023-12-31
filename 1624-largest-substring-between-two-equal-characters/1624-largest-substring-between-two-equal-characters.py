from collections import defaultdict
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        firstpos = {}
        lastpos  = defaultdict(lambda:-1)
        mx=-1
        for i in range(len(s)):
            if s[i] not in firstpos:
                firstpos[s[i]] = i
            lastpos[s[i]] = i
            mx = max(mx,lastpos[s[i]]-firstpos[s[i]]-1)
          
        return mx
            
        
        