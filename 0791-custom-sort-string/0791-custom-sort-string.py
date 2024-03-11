class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #character count in s
        charcountS = [0]*26
        for c in s:
            #count the character in s
            charcountS[ord(c)-ord('a')] += 1
        ans = ""
        for char in order:
            #traverse through order generate new permuted S
            charcount = charcountS[ord(char)-ord('a')]
            #set this char count to 0
            charcountS[ord(char)-ord('a')] = 0
            for _ in range(charcount):
                ans += char
        for index in range(26):
            #remaining character that are not in order
            charcount = charcountS[index]
            for _ in range(charcount):
                ans += chr(index + ord('a'))
        return ans