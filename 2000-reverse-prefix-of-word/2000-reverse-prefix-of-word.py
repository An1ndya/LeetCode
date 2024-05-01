class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        m = len(ch)
        wordindex = 0
        chindex = 0
        while wordindex < n and chindex < m :
            if word[wordindex] == ch[chindex]:
                wordindex += 1
                chindex += 1
            else:
                #do not match, set ch position 0
                wordindex+=1
                chindex = 0
        #means we found a match
        #so reverse the portion
        if chindex == m:
            word = "".join(reversed(word[:wordindex])) + word[wordindex:]
        return word