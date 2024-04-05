class Solution:
    def makeGood(self, s: str) -> str:
        def changeCase(w):
            upper = w.upper()
            if w == upper:
                return w.lower()
            else:
                return upper 
            
        goodstringStack = []
        length = 0 #length of good string stack
        n = len(s)
        
        for i in range(n):
            goodstringStack.append(s[i])
            length += 1
            #if more than 2 characters
            while length > 1:
                # check if s == S or S==s
                if goodstringStack[length-2] == changeCase(goodstringStack[length-1]):
                    #pop both
                    goodstringStack.pop()
                    goodstringStack.pop()
                    length -= 2
                else:
                    #to avoid infinite loop 
                    #if upper condition is false, means no more bad charcters is found
                    break
                       
        return "".join(goodstringStack)
    