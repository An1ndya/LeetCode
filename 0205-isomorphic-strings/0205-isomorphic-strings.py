class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashS = {} # map char of s to char of t
        hashT = {} # map char of t to char of s
        n=len(s)
        for i in range(n):
        
            if s[i] in hashS:
                #checked with previous mapped s to t
                if hashS[s[i]]!=t[i]:
                    return False
            if t[i] in hashT:
                #checked with previous mapped t to s
                if hashT[t[i]]!=s[i]:
                    return False
            #mapping
            hashS[s[i]]=t[i]
            hashT[t[i]]=s[i]
        return True
            