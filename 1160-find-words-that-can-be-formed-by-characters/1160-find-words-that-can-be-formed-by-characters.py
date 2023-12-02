class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charfrequency ={}
        m=len(chars)
        ans=0
        for c in chars: 
            if c in charfrequency:  charfrequency[c]+=1
            else:                   charfrequency[c]=1
        for word in words:
            n=len(word)
            if n>m: continue
            
            cf = charfrequency.copy()
            isgood=True
            for wordchar in word:
                if wordchar in cf:
                    if cf[wordchar]>0:
                        cf[wordchar]-=1
                    else:
                        isgood=False
                        break
                else:
                    isgood=False
                    break
            if isgood: ans+=n
        return ans
                    
            