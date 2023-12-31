from collections import defaultdict
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        firstpos = {}
        lastpos  = defaultdict(lambda:-1)
        
        for i in range(len(s)):
            if s[i] not in firstpos:
                firstpos[s[i]] = i
            lastpos[s[i]] = i
        mx=-1
        for char in firstpos.keys():
            mx = max(mx,lastpos[char]-firstpos[char]-1)
        return mx
            
        
        